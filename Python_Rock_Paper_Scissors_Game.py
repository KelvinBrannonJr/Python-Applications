import random

# Rock, Paper, Scissors Game 

bLoseTheGame = False

user_name = input("Let's play a game, first enter your name: ")
print(f"Welcome {user_name}, alright let's begin!")

while bLoseTheGame == False:
    user_input_choice = input("Type the full word of your choice: rock, paper, scissors, or quit: ")
    user_input_choice = user_input_choice.lower()

    if user_input_choice == "quit":
        break

    if user_input_choice != "rock" and user_input_choice != "paper" and user_input_choice != "scissors":
        print("Please choose a correct answer")
        continue

    computer_choice = random.choice(['rock','paper','scissors'])
    print(f"You chose:'{user_input_choice}' the Computer chose: '{computer_choice}'")

    if user_input_choice == computer_choice:
        print("You Tied.. try again")
        continue

    elif user_input_choice == "rock" and computer_choice == 'scissors':
        print(f"{user_name} You Win!!!")
        break
    elif user_input_choice == "paper" and computer_choice == 'rock':
        print(f"{user_name} You Win!!!")
        break
    elif user_input_choice == "scissors" and computer_choice == 'paper':
        print(f"{user_name} You Win!!!")
        break
    else:
        print(f"Sorry {user_name} You Lose, try again")
        bLoseTheGame = True