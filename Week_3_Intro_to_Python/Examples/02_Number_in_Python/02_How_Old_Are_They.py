"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    # Anton is 21 years old
    # Anton's age = 21
    anton_age = 21

    # Beth is 6 years older than Anton
    # Beth's age = 6 + Anton's age
    beth_age = 6 + anton_age

    # Chen is 20 years older than Beth
    # Chen's age = 20 + Beth's age
    chen_age = 20 + beth_age

    # Drew is as old as Chen's age plus Anton's age
    # Drew's age = Chen's age + Anton's age
    drew_age = chen_age + anton_age

    # Ethan is the same age as Chen
    # Ethan's age = Chen's age
    ethan_age = chen_age

    # Print all the friends' names and their ages
    print("Anton is " + str(anton_age))
    print("Beth is " + str(beth_age))
    print("Chen is " + str(chen_age))
    print("Drew is " + str(drew_age))
    print("Ethan is " + str(ethan_age))

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()