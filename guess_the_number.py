import random

number = random.randint(1,100)
print("WELCOME TO GUESS THE NUMBER!")
print("(The number will be between 1-100\n")

while True:
    try:
        score = int(input("Number of guesses: "))
    except ValueError:
        print("\nInvalid Score\n")
        continue

    while True:
        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("\nInvalid Guess\n")
            continue

        if score == 0:
            print("\nGame Over. You tried too many times")
            print(f"The number was: {number}")
            quit()

        if number == guess:
            print("Congratulations! You guessed the correct number.")
            print(f"Your score was: {score+1}")
            quit()

        elif number > guess:
            print("Your guess is too low.")
            score = score-1
            print(f"Your score is: {score+1}")

        elif number < guess:
            print("Your guess is too high.")
            score = score-1
            print(f"Your score is: {score+1}")

        else:
            print("Invalid Guess")