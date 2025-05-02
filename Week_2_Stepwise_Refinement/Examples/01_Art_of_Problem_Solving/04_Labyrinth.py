"""
Labyrinth.py
----------------
This will make Karel run through a labyrinth to a
corner in the upper right area.
"""

from karel.stanfordkarel import *

# Karel needs to navigate through a labyrinth
def main():
    # Karel will move forward until she reaches a wall
    # She will then rotate until she finds a clear path
    while front_is_clear(): 
        move_to_wall()
        find_direction()
    if front_is_blocked():
        turn_right()    

# Function to make Karel move to a wall
def move_to_wall():
    while front_is_clear():
        move()

# Makes Karel find a 
def find_direction():
    if right_is_clear():
        turn_right()
    if right_is_blocked():
        turn_left()

# Makes Karel turn right
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()