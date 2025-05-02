from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    run()
    end_position()

def run():
    put_beeper()
    complete_east_line()

def complete_east_line():
    alternate_to_wall()
    turn_left()
    if front_is_clear():
        start_next_line()
        turn_left()
        complete_west_line()

def complete_west_line():
    alternate_to_wall()
    turn_right()
    if front_is_clear():
        start_next_line()
        turn_right()
        complete_east_line()

def start_next_line():
    if beepers_present():
        move()
    else:
        move()
        put_beeper()

def alternate_to_wall():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()

def end_position():
    if right_is_blocked(): 
        turn_left() 
    while front_is_clear(): 
        move() 
    if right_is_clear(): 
        turn_left() 
    if front_is_blocked(): 
        turn_left() 
        while front_is_clear(): 
            move() 
        if front_is_blocked(): 
            turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()