from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint.
"""

def main():
    '''
    Expectation:
    Karel will need to move upwards twice and move to the
    east until he reaches the peak of the world.
    Once he reaches to peak, he will return to the base 
    reposition to face east and drop a beeper.
    '''
    turn_left()
    climb_peak()
    return_to_base_row()
    put_beeper()

def climb_peak():
    '''
    Expectation:
    Karel will move upwards twice and move to the right
    once.
    This pattern will repeat until he reaches the peak
    (or his front is no longer clear).
    '''
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()

def return_to_base_row():
    '''
    Expectation:
    Karel has reached the peak. 
    He should turn around, face south and move down
    until he reaches the base row.
    He will then face east.
    '''
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    
def turn_around():
    '''
    Karel will turn around 180 degrees.
    '''
    for i in range(2):
        turn_left()

def turn_right():
    '''
    Karel will turn to the right.
    '''
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()