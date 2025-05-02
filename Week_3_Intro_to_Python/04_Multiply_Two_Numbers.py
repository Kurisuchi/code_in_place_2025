"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    # Informs user that this program will multiply two numbers.
    print("This program multiplies two numbers.")
    # Requests an input as the first number or the multiplicand.
    multiplicand = int(input("Enter first number: "))
    # Requests an input as the second number or the multiplier.
    multiplier = int(input("Enter second number: "))

    # Outputs result of multiplication of multiplicand and multiplier.
    print(multiplicand * multiplier)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()