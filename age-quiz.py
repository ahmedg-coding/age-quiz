# Constants for age thresholds are defined here
AGE_THRESHOLD_DEAD = 100
AGE_THRESHOLD_RETIREMENT = 65
AGE_THRESHOLD_OVER_HILL = 40
AGE_THRESHOLD_KIDDIE_DISCOUNT = 13
AGE_THRESHOLD_21 = 21

# User input for age is obtained here
age = int(input("Enter your age: "))

# User's age is classified based on predefined criteria using constants
# This block of code checks the user's age against predefined thresholds and generates an appropriate response
if age >= AGE_THRESHOLD_DEAD:
    # User's age is determined to be 100 or older
    print("Sorry, you're dead.")
elif age >= AGE_THRESHOLD_RETIREMENT:
    # User's age is determined to be 65 or older
    print("Enjoy your retirement!")
elif age >= AGE_THRESHOLD_OVER_HILL:
    # User's age is determined to be 40 or older but less than 65
    print("You're over the hill.")
elif age < AGE_THRESHOLD_KIDDIE_DISCOUNT:
    # User's age is determined to be less than 13
    print("You qualify for the kiddie discount.")
elif age == AGE_THRESHOLD_21:
    # User's age is determined to be 21
    print("Congrats on your 21st!")
else:
    # User's age is determined to fall between 13 and 39
    print("Age is but a number.")
