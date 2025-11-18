import random
import time
def randNum():
    return random.randrange(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
print("Please select the difficulty level:"
"\n1. Easy (10 chances)"
"\n2. Medium (5 chances)"
"\n3. Hard (3 chances)")

difclt = int(input("Enter your choice: "))

if difclt == 1:
    print("Great! You have selected the Easy difficulty level." "\nLet's start the game!")
    chances = 10
elif difclt == 2:
    print("Great! You have selected the Medium difficulty level.""\nLet's start the game!")
    chances = 5
elif difclt == 3:
    print("Great! You have selected the Hard difficulty level.""\nLet's start the game!")
    chances = 3

def guessnum(chances, ranNum):
    myChances = 0
    while myChances < chances :
        start = time.time()
        guesserNum = int(input("Enter your guess: "))
        print(ranNum)
        if guesserNum != ranNum:
            chances += 1
            if guesserNum > ranNum:
                print(f"Incorrect! The number is less than {guesserNum}.")
                myChances+=1
            else:
                print(f"Incorrect! The number is greater than {guesserNum}.")
                myChances += 1
        else:
            print(f"Congratulations! You guessed the correct number in {myChances+1} attempt(s)."
                  f"\nYour guess time is {round(time.time()- start)} s.")
            quit()
    if chances == 0:
        print("You've lost")
        quit()

    return 0
guessnum(chances, randNum())