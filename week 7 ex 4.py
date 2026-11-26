import csv

with open("students.csv",'r') as file:
    data = csv.reader(file)

    for row in data:
        print(row[0], row[1], row[2])

# a = 1 2 3 4 ==> Values
# i = 0 1 2 3 ==> index
#print(a[1]