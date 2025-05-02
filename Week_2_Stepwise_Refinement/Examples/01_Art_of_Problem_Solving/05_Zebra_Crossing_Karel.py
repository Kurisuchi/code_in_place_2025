"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel will create a zebra crossing.
    Pattern is 2-square wide column of beepers,
    followed by repeating pairs of 3-square wide gap,
    and a 2-squared wide column of beepers
    """
    while front_is_clear():
        # Karel will paint the 2 rows of beepers as columns
        paint_columns()

        # Rotate Karel counterclockwise if the front is blocked
        if front_is_blocked():
            turn_left()

        # Move Karel to the next start of the column if the front is clear
        if front_is_clear():
            move_to_next_row()

# Karel will paint the 2 rows of beepers as columns
def paint_columns():
    turn_left()
    paint_column()
    turn_right()
    move()
    turn_right()
    paint_column()

# Karel will move to the next point for the next set of columns
def move_to_next_row():
    for i in range(4):
        move()

# Makes Karel drop one vertical column of beepers
def paint_column():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

# Makes Karel rotate clockwise
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()