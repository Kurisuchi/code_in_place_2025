"""
This program should convert an inputted Fahrenheit temperature and print out its equivalent in Celsius.
"""

def main():
    # Ask for a temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    # Print out the converted value
    print("Temperature: " + str(degrees_fahrenheit) + "F = " + str(degrees_celsius) + "C")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()