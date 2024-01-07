import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? : ").lower()

    print("Computer:", computer)
    print("Player:", player)

    if player == computer:
        print("Tie!")

    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
        elif computer == "rock":
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
        elif computer == "paper":
            print("You win!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        elif computer == "scissors":
            print("You win!")
    player_again = input("player again ? (yes/no): ").lower()
    if player_again !="yes":
        break
print("BYE!See you again")

