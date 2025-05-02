"""
Example of a Fill in the Blank program, like the one from the lesson.
The user will enter three words (a color, an adjective and a goal).
We will then turn them into a one sentence story.
"""

def main():
    # Ask for a color input
    color = input("A color: ")
    # Ask for an adjective input
    adjective = input("An adjective: ")
    # Ask for a goal input
    goal = input("A goal you would like to achieve: ")

    # Will print the sentence:
    # At dawn the sky turned <color>, and the air felt <adjective>. I decided I will finally <goal>.
    print("At dawn the sky turned " + color + ", and the air felt " + adjective + ". I decided today I will finally " + goal + ".")

if __name__ == "__main__":
    main()