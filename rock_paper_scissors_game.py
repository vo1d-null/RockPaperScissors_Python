import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input("Choose your fighter : [r]ock , [p]aper , [s]cissors \n")
if player_move == "r" and "Rock" and "R" and "rock":
    player_move = rock
elif player_move == "s" and "scissors" and "Scissors" and "S":
    player_move = scissors
elif player_move == "p" and "Paper" and "P" and "Paper":
    player_move = paper
else:
    raise SystemExit("Invalid input.Try Again!")

computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_random_number == 1:
    computer_move = rock
    print("The computer chose rock!")
elif computer_random_number == 2:
    computer_move = paper
    print("The computer chose paper!")
else: computer_move = scissors
print("The computer chose scissors!")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")

if (player_move == rock and computer_move == rock) or \
        (player_move == paper and computer_move == paper) or \
        (player_move == scissors and computer_move == scissors):
    print("Draw!")

if (player_move == rock and computer_move == paper) or \
        (player_move == paper and computer_move == scissors) or \
        (player_move == scissors and computer_move == rock):
    print("You lose!")
