# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui

range_num = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_num
    secret_num = random.randrange(0, range_num)
    print "Welcome to this game!"
    print "Now you should input a number from 0 to %r" % range_num

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_num
    range_num = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_num
    range_num = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    guess_num = int(guess)
    print "Guess was %r." % guess_num
    
    if guess_num < secret_num:
        print "Higher"
    elif guess_num > secret_num:
        print "Lower"
    else:
        print "Correct"
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
button1 = frame.add_button("range [0, 100)", range100)
button2 = frame.add_button("range [0, 1000)", range1000)

inp = frame.add_input("Input your guess", input_guess, 100)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric