# Rock, Paper, Scissors
  
print('=====================')
print('Rock, Paper, Scissors')
print('=====================')

import random
player = 0
computer = 0

print('1) ✊')
print('2) ✋')
print('3) ✌️')

player = int(input('Pick a number: '))

while player > 3:
  player = int(input('Invalid number. Pick again: '))

if player == 1:
  print('You chose: ✊')
elif player == 2:
  print('You chose: ✋')
elif player == 3:
  print('You chose: ✌️')

computer = random.randint(1, 3)

if computer == 1:
  print('Computer chose: ✊')
elif computer == 2:
  print('Computer chose: ✋')
elif computer == 3:
  print('Computer chose: ✌️')

if player == computer:
  print('Tie!')
elif player == 1 and computer == 3:
  print('You win!')
elif player == 2 and computer == 1:
  print('You win!')
elif player == 3 and computer == 2:
  print('You win!')
elif player == 3 and computer == 1:
  print('Computer wins!')
elif player == 1 and computer == 2:
  print('Computer wins!')
elif player == 2 and computer == 3:
  print('Computer wins!')
