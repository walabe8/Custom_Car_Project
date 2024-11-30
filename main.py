# Intro
print("Welcome to the UMBC \n Car Customization Form!")
print()

# Make & Model Form 1-2
print(
    "(For multiple choice problems, please enter the letter of the selection you're looking for"
)
print("~ Make & Model~")
print("1. What Model of Car are you ordering?")
print("    a. Honda Civic")
print("    b. Honda CRV")
print("    c. ")
print("    d. ")

print()
userPrompt = input("Please enter 'a' - 'd': ")

print()
print(
    "2. Would you like to upgrade from the 4-door option to the 2-door option?"
)
userPrompt2 = input("Please enter 'yes' or 'no': ")

# Exterior Form 3-4
print()
print("Exterior")
print("3. What color would you like your care to be?")
userPrompt3 = input("You may enter the name of any color you'd like:")

print()
print("4. Would you like the deluxe weather package?")
userPrompt4 = input("Please enter 'yes' or 'no': ")

# Interior Form 5-6
print()
print("Interior")
print("5. Which Engine would you like your car to have?")
print("    a. Electric")
print("    b. V8")
print("    c. V6")
userPrompt5 = input("Please enter 'yes' or 'no': ")

print()
print("6. Would you like heated seats?")
userPrompt6 = input("Please enter 'yes' or 'no': ")

# Summary of their responses and corresponding questions should be shown at the end
print()
print("Summary")
print(f"Model Option: {userPrompt}")
print(f"Upgrade to 2-Door?: {userPrompt2}")
print(f"Desired Color?: {userPrompt3}")
print(f"Upgrade to Deluxe Weather?: {userPrompt4}")
print(f"Engine Option?: {userPrompt5}")
print(f"Upgrade to Heated Seats?: {userPrompt6}")
