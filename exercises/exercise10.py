
def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


age_calculator = int(input("What is your age of birth? "))
age = get_age(age_calculator)
if age <= 120:
    print(age)
else:
    print("How are you still alive?")
