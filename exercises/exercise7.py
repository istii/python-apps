try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = (value * 100) / total_value
    print(f"That is {percentage}%")
except ValueError:
    exit('You need to enter a number. Run the program again.')
except ZeroDivisionError:
    print("Your total value cannot be zero.")