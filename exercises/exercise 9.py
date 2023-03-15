password = input("Enter password: ")


def password_strength():
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["results"] = digit
    upper = False
    for i in password:
        if i.isupper():
            upper = True
    result["uppercase"] = upper
    if all(result.values()):
        return "Strong password!"
    else:
        return "Weak password!"


print(password_strength())
