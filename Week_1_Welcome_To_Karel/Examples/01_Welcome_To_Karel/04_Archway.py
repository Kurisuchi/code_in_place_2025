"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    ascend_wall()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    descend_wall()

# This makes Karel turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This will make Karel scale the wall
def ascend_wall():
    # Karel will perform actions while his right is blocked
    while right_is_blocked():
        if front_is_clear():
            move()
        else:
            turn_left()

# This will make Karel go down the wall
def descend_wall():
    while front_is_clear():
        move()
        if front_is_blocked():
            turn_left()
            
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()