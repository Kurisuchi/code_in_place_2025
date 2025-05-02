from karel.stanfordkarel import *

def main():
    # Karel will only move if there's a beeper present
    while(beepers_present()):
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()