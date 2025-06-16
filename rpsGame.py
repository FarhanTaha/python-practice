# Code from Automate the Boring stuff with Python 

import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print(f'\nWins: {wins}, Losses: {losses}, Ties: {ties}') # my improvement
    # print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # main code
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower() # my improvement
        # playerMove = input() # main code
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1



#CHATGPT IMPROVEMENT

# import random

# print('ROCK, PAPER, SCISSORS')

# wins = 0
# losses = 0
# ties = 0

# while True:
#     print(f'\nWins: {wins}, Losses: {losses}, Ties: {ties}')
#     print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#     playerMove = input().lower()

#     if playerMove == 'q':
#         print("Thanks for playing!")
#         break
#     if playerMove not in ['r', 'p', 's']:
#         print("Invalid input. Please type 'r', 'p', 's', or 'q'.")
#         continue

#     moves = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
#     print(f"{moves[playerMove]} versus...")

#     computerMove = random.choice(['r', 'p', 's'])
#     print(moves[computerMove])

#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties += 1
#     elif (playerMove == 'r' and computerMove == 's') or \
#          (playerMove == 'p' and computerMove == 'r') or \
#          (playerMove == 's' and computerMove == 'p'):
#         print('You win!')
#         wins += 1
#     else:
#         print('You lose!')
#         losses += 1
