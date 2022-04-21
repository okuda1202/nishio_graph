import csv
import pprint

with open('data/temp/sample_writer_row.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])

with open('data/temp/sample_writer_row.csv') as f:
    print(f.read())
