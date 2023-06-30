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


choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choise = random.randint(0, 2)

if choise == 0:
    print("Your choice")
    print(rock)
    if computer_choise == 0:
        print("Computer choise\n")
        print(rock)
        print("Tie!")
    elif computer_choise == 1:
        print("Computer choise\n")
        print(paper)
        print("You lose!")
    elif computer_choise == 2:
        print("Computer choise\n")
        print(scissors)
        print("You win!")
elif choise == 1:
    print("Your choice")
    print(paper)
    if computer_choise == 0:
        print("Computer choise\n")
        print(rock)
        print("You win!")
    elif computer_choise == 1:
        print("Computer choise\n")
        print(paper)
        print("Tie!")
    elif computer_choise == 2:
        print("Computer choise\n")
        print(scissors)
        print("You lose!")
elif choise == 2:
    print("Your choice")
    print(scissors)
    if computer_choise == 0:
        print("Computer choise\n")
        print(rock)
        print("You lose!")
    elif computer_choise == 1:
        print("Computer choise\n")
        print(paper)
        print("You win!")
    elif computer_choise == 2:
        print("Computer choise\n")
        print(scissors)
        print("Tie!")
