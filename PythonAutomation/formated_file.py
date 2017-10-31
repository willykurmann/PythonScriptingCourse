import csv

with open("data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("data2.csv","r") as file:
    reader = csv.reader(file,  delimiter=',')
    for row in reader:
        print(row)
        print(row[0])