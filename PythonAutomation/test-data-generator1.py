from faker import Faker
import csv

data = Faker()

users = []
for i in range(1,11):
    user = "{},{},{}".format(data.name(), data.email(), data.city())
    users.append(user)

with(open("users.txt","w")) as file:
    for user in users:
        file.write(user + '\n')

with open("users.txt", "r") as file:
    reader = csv.reader(file,delimiter=',')
    for row in reader:
        print(row[0] + " / " + row[1] + " / " + row[2])

