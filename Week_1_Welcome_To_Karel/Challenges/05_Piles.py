from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    
    # Pick up beepers.
    pick_ten_beepers()

    # Move to 2nd beeper location and pick up beepers.
    move()
    move()
    pick_ten_beepers()

    # Move to 3rd beeper location and pick up beepers.
    move()
    move()
    pick_ten_beepers()

    # Karel moves to the east
    move()

# This function will make Karel pick up 10 beepers.
def pick_ten_beepers():
    for i in range(10):
        pick_beeper()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()