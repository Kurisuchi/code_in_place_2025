from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    This code will move to the beeper location and pick it up.
    Move to the puzzle and put the beeper there.
    Finally, return to the initial location.
    """
    # To beeper location and pickup
    move_and_pick()

    # To complete square
    drop_puzzle()

    # To return to initial position
    return_to_initial_position()

def move_and_pick():
    '''
    This is to move to the beeper location and pick it up.
    '''
    move()
    move() 
    pick_beeper()

def drop_puzzle():
    '''
    This is to place the beeper in the puzzle
    '''
    move()
    turn_left()
    move()
    move()
    put_beeper()

def return_to_initial_position():
    '''
    This is to return Karel to its original position.
    '''
    turn_left()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_left()
    turn_left()

def turn_right():
    '''
    This is to turn right by turning left three times.
    '''
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()