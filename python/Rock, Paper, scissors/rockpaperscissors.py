import random

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
game_images = [rock, paper, scissors]
user_input = int(input(
    "Welcome to rock, paper, scissors game! Chose between paper - 1, rock - 0 or scissors - 2\n"))
print(game_images[user_input])
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

if user_input >= 3:
    print("you typed wrong number!")

elif user_input == 0 and computer_choice == 2:
    print("you win!")

elif user_input == 2 and computer_choice == 2:
    print("you lose!")

elif user_input < computer_choice:
    print("you lose!")

elif user_input > computer_choice:
    print("you win!")

elif user_input == computer_choice:
    print("its a draw")
