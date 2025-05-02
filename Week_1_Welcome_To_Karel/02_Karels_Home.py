from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move_to_right_corner()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    return_home()

# Makes Karel move to the right corner of the inner square
def move_to_right_corner():
    move()
    move()

# Makes Karel return to her initial position
def return_home():
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()

# Makes Karel turn to the other side
def turn_around():
    turn_left()
    turn_left()

# Makes Karel turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()