import csv

records = [
["ID", "Name", "Marks"],
[1, "Amal", 63],
[2, "Roger", 70],
[3, "Anzhelina", 68],
[4, "Zenata", 70],
[5, "Luis", 70],
[6, "Antonio", 63],
[7, "Constantin", 67],
[8, "Marcin", 68],
[9, "Dariusz", 65],
[10, "Nikoletta", 63],
]

with open("students.csv", 'w', newline='') as file:
 data = csv.writer(file)
 data.writerows(records)

print("Student CSV file Created....!")