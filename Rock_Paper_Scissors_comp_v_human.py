#Rock, Paper, Scissors Game Player vs Computer
import random
def get_user_choice(): #Function to get user's choice
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice
def get_computer_choice(): #Function to get computer's choice
    print("The computer is making its choice...")
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice
x=get_user_choice()
y=get_computer_choice()
if x == y: #Check if both choices are the same
    print(f"Both players chose {x}. It's a tie!")
elif (x == 'rock' and y == 'scissors') or (x == 'paper' and y == 'rock') or (x == 'scissors' and y == 'paper'): #Check if user wins
    print(f"You chose {x} and the computer chose {y}. You win!")
else: #If not a tie or user win, then computer wins
    print(f"You chose {x} and the computer chose {y}. You lose!")