import random
random_int = random.randint(0,2)

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
game_images = [ rock, paper, scissors]
choice_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice_int == 0:
    choice = "rock"
elif choice_int == 1:
    choice = "paper"
elif choice_int == 2:
    choice = "scissors"

print(game_images[choice_int])

if random_int == 0:
    computer_choice = "rock"
elif random_int == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

print(f"Computer chose:")
print(game_images[random_int])

if computer_choice == choice:
    print(f"It's a tie!")
elif computer_choice == "rock" and choice == "paper":
    print(f"You win!")
elif computer_choice == "rock" and choice == "scissors":
    print(f"You lose!")
elif computer_choice == "paper" and choice == "rock":
    print(f"You lose!")
elif computer_choice == "paper" and choice == "scissors":
    print(f"You win!")
elif computer_choice == "scissors" and choice == "rock":
    print(f"You win!")
elif computer_choice == "scissors" and choice == "paper":
    print(f"You lose!")