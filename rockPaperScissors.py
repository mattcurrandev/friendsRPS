import random, sys

print('Rock, Paper, Scissors')
wincount = 0
tiecount = 0
losecount = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wincount, losecount, tiecount))
    while True:
        print('Enter your move (r)ock (p)aper (s)cissors or (q)uit')

        move = input()

        if move == 'q':
            sys.exit()
        if move == 'r' or move == 's' or move == 'p' or move == 'f':
            break
        print('Type one of the following r, p, s')

    if move == 'r':
        print('ROCK versus.....')
    elif move == 'p':
        print('PAPER versus.....')
    elif move == 's':
        print('SCISSORS versus.....')
    elif move == 'f':
        print('Fire, beats everything!')
        print('.......')
        print('Oh really, does it beat water baloon?')
        
    
        
    randomNumber = random.randint(1,3)

    if move == 'f':
        continue
    elif randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
    if move == computerMove:
        print("It's a Tie")
        tiecount = tiecount + 1
    elif move == 'r' and computerMove == 's':
        print("You Won!")
        wincount = wincount + 1
    elif move == 's' and computerMove == 'p':
        print("You Won!")
        wincount = wincount + 1
    elif move == 'p' and computerMove == 'r':
        print("You Won!")
        wincount = wincount + 1
    elif move == 'p' and computerMove == 's':
        print('You Lost')
        losecount = losecount + 1
    elif move == 's' and computerMove == 'r':
        print('You Lost')
        losecount = losecount + 1
    elif move == 'r' and computerMove == 'p':
        print('You Lost')
        losecount = losecount + 1