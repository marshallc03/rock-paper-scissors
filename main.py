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

#Write your code below this line 👇
import random

user_draw = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
computer_draw = random.randint(0,2)

choices = [rock, paper, scissors]

print(choices[user_draw])
print("Computer chose: \n")
print(choices[computer_draw])

if user_draw == computer_draw:
  print("It's a draw!")
elif user_draw == 0 and computer_draw == 2:
  print("You win!")
elif computer_draw > user_draw:
  print("You lose.")
elif computer_draw == 0 and user_draw == 2:
  print("You lose.")
elif user_draw > computer_draw:
  print("You win!")
else:
  print("Unable to draw.")