
filenames = ["File1.txt", "File2.txt", "File3.txt"]

for filename in filenames:
    file = open(f"../files/{filename}", "w")
    file.write("Hello")
    file.close()