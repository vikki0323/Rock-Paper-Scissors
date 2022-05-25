import random

print('Welcome to Rock, Paper, Scissors!')
user_actions = input('Please Select Rock, Paper, or Scissors: ')
actions = ("Rock", "Paper", "Scissors")
comp_actions = random.choice(actions)

print(f'You Selected {user_actions}, Computer Selcted {comp_actions}.')

if user_actions == comp_actions:
    print('It is a Draw! Try again!')
elif user_actions == "Rock":
    if comp_actions == "Paper":
        print("Computer Wins Round! Paper Beats Rock!")
    else:
        print("Player Wins Round! Rock Beats Scissors!")
elif user_actions == "Paper":
    if comp_actions == "Scissors":
        print("Computer Wins Round! Scissors Beats Paper! So Close.")
    else:
        print("Player Wins Round! Paper Beats Rock!")
elif user_actions == "Scissors":
    if comp_actions == "Rock":
        print("Computer Wins Round! Rock Beats Scissors! So Close.")
    else:
        print("Player Wins Round! Scissors Beats Paper!")
