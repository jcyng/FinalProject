"""
This script is essentially a number guessing game. 
The user enters two user arguments: a minimum and a maximum integer (in that order) that creates a range in which an integer is randomly generated.
The user then guesses an integer within that range until it matches the randomly generated integer.
Based on the guess, the system will let the user know whether to go higher or lower on the next guess.
The script also keeps track of user's previous guesses, and counts how many guesses the user made within a certain tens digit range (e.g. if user guessed 30 and 31, that is twice in the "3" tens digit range)
If the same number is guessed twice, the script will tell the user that this number was already guessed previously.
Once the user guesses the correct integer, the script will let the user know how many guesses it took the user to make that guess. Then the system exits.
Note: The user arguments need to be integers (positive or negative), with the first argument/integer < second argument/integer. 
If a non-integer is entered (e.g. a string, a float), and/or first argument > second argument, the system will capture that error and make the user guess a range between 1 - 10.
If the guess is a non-integer (e.g. a string, a float), the system will capture that error and let the user know that was not a valid integer. Then ask the user to guess again.
"""

import random
import sys

def chosen_range(low, high):
    try:
        return random.randint(int(low), int(high))
    except ValueError:
        print ("Those arguments are not valid. Now just guess an integer from 1 to 10! (And ignore the next sentence)")
        return random.randint(1,10)

my_min = sys.argv[1]
my_max = sys.argv[2]

secret_number = chosen_range(my_min, my_max)
guess_list = []
tens_tracker = {}

while True:
    try:
        guess = int(input('Guess an integer from {} to {}: '.format(my_min, my_max)))
    
        tens_digit = int(guess/10)
        if (tens_digit not in tens_tracker):
            tens_tracker[tens_digit] = 1
        else:
            tens_tracker[tens_digit] += 1;
    
        if (guess in guess_list):
         print("You already guessed this number silly!")
         continue

        guess_list.append(guess)

        if guess < secret_number:
            print('Nope, go higher')

        elif guess > secret_number:
            print('Nope, go lower')

        else:
            print('You guessed it! The number was {}'.format(secret_number))
            print('You guessed it in {} attempts'.format(len(guess_list)))
            break
        print('Previous guesses: {}'.format(guess_list))
        print("The number of guesses you've made in these ten's digits: {}".format(tens_tracker))

    except NameError:
        print ("That was not a valid integer!")
    except ValueError:
        print ("That was not a valid integer!")
