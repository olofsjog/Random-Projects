import random
import re

score = 0
list = ["rock", "paper", "scissors"]

print("WELCOME TO ROCK, PAPER, SCISSORS")
print("--------------------------------")

while True:
    try:
        player = input("\nRock [R], Paper [P], Scissors [S]: ")
    except ValueError:
        print("Error")
        continue

    regex = r"[r,R]ock|[p,P]aper|[s,S]cissors"

    if re.match(regex, player.lower()):
        print("yes")

        num = random.randint(0, 2)
        opponent = list[num]

        if (player.lower() == "r" or player.lower() == "rock") and opponent == "scissors":
            print("You win!")
            score += 1
        elif (player.lower() == "r" or player.lower() == "rock") and opponent == "paper":
            print("You lose!")
        elif (player.lower() == "p" or player.lower() == "paper") and opponent == "scissors":
            print("You lose!")
            score -= 1
        elif (player.lower() == "p" or player.lower() == "paper") and opponent == "rock":
            print("You win!")
            score += 1
        elif (player.lower() == "s" or player.lower() == "scissors") and opponent == "rock":
            print("You win!")
            score += 1
        elif (player.lower() == "s" or player.lower() == "scissors") and opponent == "paper":
            print("You lose!")
            score -= 1
        else:
            print("Draw!")

    else:
        print("Incorrect Sign")