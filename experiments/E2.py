import csv

with open("weather.csv") as file:
    data = list(csv.reader(file))


city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])

