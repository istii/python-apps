password = input("Enter new password: ")

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

print(result)

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
