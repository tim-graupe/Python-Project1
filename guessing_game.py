"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

name = input('What is your name?  ')
print("Welcome to the number guesser, {}. Your task is to guess the number between 1 - 10".format(name))


def start_game():
    attempts = 0
    ran_num = random.randint(1, 10)
    guess = int(input("I am thinking of a number between 1 - 10, what is it?  "))
    attempts +1
    while guess != ran_num:
        attempts +=1
        try:
            guess = int(input("Guess the number, 1 - 10."))
            if guess < 1:
                raise ValueError
            elif guess > 10:
                raise ValueError
            if guess > ran_num:
                print("That guess was a little high, try guessing lower.")
            elif guess < ran_num:
                print("That was too low. Guess higher!")
        except ValueError:
            print("Please enter a valid number.")


    if attempts == 0:
        print("You got it on the first try! Are you cheating?")
    else:
        print("Winner winner chicken dinner! It took you {} attempts to get it.".format(attempts + 1))
    if attempts < high_score:
        high_score == attempts
        print("New high score!")
    play_again = str(input("Would you like to play again? Y/N").upper())
    if play_again == "Y":
      print("Game on! Can you beat your previous high score of {}?".format(high_score))
      start_game()
    elif play_again == "N":
        print("That was fun! Hope we play again soon!")
        
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()