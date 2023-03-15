# Coding Exercise 1
# Create a program that does the following:
#
# 1. Prompts the user to input the country they are from.
#
# 2. If the user enters the word USA, the program prints out Hello.
#
# 3. If the user enters the word  India, the program prints out Namaste.
#
# 4. If the user enters the word Germany, the program prints out Hallo.
#
# Note: Strings are case-sensitive in Python, meaning germany and Germany are treated as two different strings.
#
# Solution
while True:
    user_input = input("Where do you come from? ")
    match user_input:
        case "USA" | "usa":
            print("Hello")
        case "India" | "india":
            print("Namaste")
        case "Germany" | "germany":
            print("Hallo")
        case _:
            print("Welcome")

#
#
# Coding Exercise 2
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# Copy-paste the above line into your IDE and write a for-loop below that line that makes the program produce the following output:
#
#
#
#
# Tip:  Use the str.title() method to convert strings to Title Case.