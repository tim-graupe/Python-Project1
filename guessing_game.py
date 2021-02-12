
import random

name = input('What is your name?  ')
print("Welcome to the number guesser, {}. Your task is to guess the number between 1 - 10".format(name))


def start_game():
    attempts_left = 11
    ran_num = random.randint(1, 10)
    while attempts_left != 0:
        attempts_left -= 1
        try:
            guess = int(input("Guess the number, 1 - 10."))
            if guess == ran_num:
              break
            elif guess < 1:
                raise ValueError
            elif guess > 10:
                raise ValueError
            if guess > ran_num:
                print("That guess was a little high, try guessing lower.")
            elif guess < ran_num:
                print("That was too low. Guess higher!")
        except ValueError:
            print("Please enter a valid number.")


    if attempts_left == 10:
        print("You got it on the first try! Are you cheating?")
    elif attempts_left == 0:
        print("You are out of tries, better luck next time! The magic number was {}".format(ran_num))
    else:
      print("Winner winner chicken dinner! It took you {} attempts to get it.".format(10 - attempts_left))
    try:
      
      play_again = str(input("Would you like to play again? Y/N").upper())
    except ValueError:
           print("Please enter Y or N")
    if play_again == "Y":
        print("Game on!")
        start_game()
    elif play_again == "N":
        print("That was fun! Hope we play again soon!")


start_game()