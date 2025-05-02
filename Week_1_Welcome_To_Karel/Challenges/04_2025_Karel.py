from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 25 beepers, and end facing East to 
the right of the 25 beepers.
"""

def main():
    # Place 20 beepers
    for i in range(20):
        put_beeper()
    
    # Move 1 step and place 25 beepers
    move()
    for i in range(25):
        put_beeper()

    # Move to the east
    move()

if __name__ == '__main__':
    main()