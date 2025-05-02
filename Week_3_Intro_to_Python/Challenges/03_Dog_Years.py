# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    # Ask for an age input to be calculated to dog years
    age = input("Enter an age in calendar years: ")

    # Multiply the age with the dog years multiplier
    # Save the result to the "dog_years" variable
    dog_years = float(age) * DOG_YEARS_MULTIPLIER

    # Print the sentence:
    # That's <dog_years> in dog years!
    print("That's " + str(dog_years) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()