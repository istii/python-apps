filenames = ['document', 'report', 'presentation']

for i, filename in enumerate(filenames):
    row = f"{i}-{filename.capitalize()}.txt"
    print(row)
