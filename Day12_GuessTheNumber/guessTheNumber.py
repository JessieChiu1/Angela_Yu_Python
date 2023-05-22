import random


def guessNumGame():
    print("Welcome to Guess the Number Game!")
    level = input("Chooses 'easy' or 'hard' difficulty level").lower()
    if level == "easy":
        lives = 10
    else:
        lives = 5

    gameOver = False
    num = random.randint(0, 101)
    while lives > 0 or not gameOver:
        guess = int(input("Pick a Number between 1 and 100 \n"))
        if num == guess:
            print(f"You guess the number: {num}")
            gameOver = True
        elif num > guess:
            print("Too low! Guess Again!")
            lives -= 1
            print(f"You have {lives} lives left")
        else:
            print("Too High! Guess Again!")
            lives -= 1
            print(f"You have {lives} lives left")


guessNumGame()
