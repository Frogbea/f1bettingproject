# USERNAME and password component
import csv

with open("students.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
