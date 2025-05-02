from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        for i in range(4):
            build_column()
            turn_around()
            reset_to_base()
            if front_is_clear():
                move_to_next_column()

def build_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_around():
    turn_left()
    turn_left()

def reset_to_base():
    while front_is_clear():
        move()
    turn_left()

def move_to_next_column():
    for i in range(4):
        move()

if __name__ == '__main__':
    main()