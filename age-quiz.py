AGE_THRESHOLD_DEAD = 100
AGE_THRESHOLD_RETIREMENT = 65
AGE_THRESHOLD_OVER_HILL = 40
AGE_THRESHOLD_KIDDIE_DISCOUNT = 13
AGE_THRESHOLD_21 = 21

age = int(input("Enter your age: "))

if age >= AGE_THRESHOLD_DEAD:
    print("Sorry, you're dead.")
elif age >= AGE_THRESHOLD_RETIREMENT:
    print("Enjoy your retirement!")
elif age >= AGE_THRESHOLD_OVER_HILL:
    print("You're over the hill.")
elif age < AGE_THRESHOLD_KIDDIE_DISCOUNT:
    print("You qualify for the kiddie discount.")
elif age == AGE_THRESHOLD_21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")
