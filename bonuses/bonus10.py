try:
    witdh = float(input("Enter rectangle width: "))
    lenght = float(input("Enter rectangle length: "))

    if witdh == lenght:
        exit("That looks like a square")

    area = witdh * lenght
    print(area)
except ValueError:
    print("Please enter a number.")
