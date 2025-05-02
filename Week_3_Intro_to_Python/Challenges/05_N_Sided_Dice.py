import random

# This program will create a randomized roll output
# based on the number of sides your dice has.
def main():
    # Asks for the number of sides your dice has
    dice_sides = int(input("How many sides does your dice have? "))

    # Calculates the roll output from 1 to the 
    # number of sides
    # Example: 6-sided dice can have an output of 1 to 6
    roll = random.randint(1, dice_sides)

    # Prints final roll result
    print("Your roll is " + str(roll))

if __name__ == '__main__':
    main()