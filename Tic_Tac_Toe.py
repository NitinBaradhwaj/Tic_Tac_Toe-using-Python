#tic_tac_toe
#game
#in python
#code goes here...
squares = [' ']*9
players = 'OX'
board = '''
  -----------------
   0     1     2
  {0}   | {1}   | {2}
  -----------------
3 {3}   | {4}   | {5}    5
  -----------------
  {6}   | {7}   | {8}
   6     7     8
  -----------------
'''
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals winning
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals winning
    (0, 4, 8), (2, 4, 6)             # diagonals winning
]

def check_who_wins(player):
    for m, n, o in win_conditions:
        if {squares[m], squares[n], squares[o]} == {player}:
            return True

while True:
    print(board.format(*squares))
    if check_who_wins(players[1]):
        print(f'{players[1]} is the winner!')
        print(f'Congratulations!! {players[1]}')
        break
    if ' ' not in squares:
        print('Game Over!')
        print('GO Back to restart')
        break
    move = input(f'{players[0]} to move [0-8] > ')
    if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
        print('Invalid move!')
        print('Please select another number..')
        continue
    squares[int(move)], players = players[0], players[::-1]
