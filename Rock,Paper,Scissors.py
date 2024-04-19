from random import randint

playagain = 'y'
while (playagain == 'y'):
  player = input('rock, paper or scissors?')
  print(player, 'vs', end=' ')

  chosen = randint(1,3)
  #print(chosen)
  if chosen == 1:
    computer = 'rock'

  elif chosen == 2:
    computer = 'paper'

  else:
    computer = 'scissors'

  print(computer)

  if player == computer:
    print('DRAW')

  elif player == 'rock' and computer == 'paper':
    print('COMPUTER WINS')

  elif player == 'rock' and computer == 'scissors':
    print('YOU WIN')

  elif player == 'paper' and computer == 'scissors':
    print('COMPUTER WINS')

  elif player == 'paper' and computer == 'rock':
    print('YOU WIN')

  elif player == 'scissors' and computer == 'rock':
    print('YOU WIN')

  elif player == 'scissors' and computer == 'paper':
    print('COMPUTER WINS')

  playagain = input('Play again ? y/n')
