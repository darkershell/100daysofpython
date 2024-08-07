rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
import sys
game_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)
print("computer chose:")
try:
    print(game_images[player])
except IndexError:
    print("You typed an invalid number, you lose!")
    sys.exit()

print("computer chose:")
print(game_images[computer])

if player >= 3 or player < 0:
	print("You typed an invalid number, you lose!")
elif player == 0 and computer == 2:
	print("You win!")
elif computer == 0 and player == 2:
	print("You lose")
elif computer > player:
	print("You lose")
elif player > computer:
	print("You win!")
elif computer == player:
	print("It's a draw")