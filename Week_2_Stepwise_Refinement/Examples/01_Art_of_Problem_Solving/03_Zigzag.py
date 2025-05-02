"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    # Karel moves from left to right, dropping beepers
    # alternately starting from her starting point
    while front_is_clear():
        place_beepers()

    # Karel will rotate counterclockwise if she hits the
    # wall
    turn_left()

    # Karel will continue dropping beepers alternately.
    while front_is_clear():
        place_beepers()

    # Karel will rotate counterclockwise if she hits the
    # wall
    turn_left()

    # Karel will move until she hits the bottom right wall
    reset()
    
# Makes Karel drop beepers alternately
def place_beepers():
    put_beeper()
    move()
    # If Karel's front is clear, she will continue moving
    if front_is_clear():
        move()
    # If Karel's front is blocked, she will rotate left
    # and move 1 step
    if front_is_blocked():
        turn_left()
        move()

# Makes Karel return to the leftmost point in the row
def reset():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()