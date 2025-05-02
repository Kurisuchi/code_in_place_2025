"""
This program will flip a weighted coin.
This will use the random module and "flip" coin where the probability of heads is 70%
and print the outcome (heads or tails).
"""

import random

HEADS_WEIGHT = 0.7 # 70%

def main():
    # Use random.random() to generate a decimal number from 0.0 to 1.0
    # If the randomly generated number is less than 0.7 (the weight for heads), it's heads!
    if random.random() < HEADS_WEIGHT:
        print("Heads!")
    else:
        print("Tails!")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()