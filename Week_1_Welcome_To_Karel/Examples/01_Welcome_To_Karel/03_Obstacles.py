"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    move()
    for i in range(3):
        place_beeper_obstacle()
    move()
    move()


def place_beeper_obstacle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()