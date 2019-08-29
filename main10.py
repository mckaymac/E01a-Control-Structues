#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # prints 'Greetings!'
colors = ['red','orange','yellow','green','blue','violet','purple']  # builds an array of strings
play_again = ''                     # sets the play_again variable to ''
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):       # sets up a conditional statement that will go until play_again = 'n' and play_again = 'no'
    match_color = random.choice(colors)                 # sets the match_color variable to a random string in colors
    count = 0                                           # sets count variable to 0
    color = ''                                          # sets color to ''            
    while (color != match_color):                       # sets up a conditional statement that will go until color = match_color 
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()                   # sets color to all lowercase and gets rid of empty characters/spaces
        count += 1                                      # adds one to count
        if (color == match_color):                      # sets up a conditional statement that happens if color != match_color
            print('Correct!')                           # if condition is met then program prints 'Correct!'
        else:                                           # if previous if statement is not met then this is executed
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # prints a statement along with number of guesses if user answers incorrectly
    print('\nYou guessed it in {0} tries!'.format(count))  # prints a statement with the number of tries
    if (count < best_count):                            # sets up conditional statement that executes if count is less than best_count
        print('This was your best guess so far!')       # prints a statement 
        best_count = count                              # sets best_count variable to count
    play_again = input("\nWould you like to play again? ").lower().strip() # prints statement asking user if they want to play again
print('Thanks for playing!')                            # prints 'Thanks for playing!'