filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"D:\Desktop\python course downloads\{filename}", 'r')
    content = file.read()
    print(content)