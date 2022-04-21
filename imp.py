import csv
import pprint

with open('data/src/sample.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
