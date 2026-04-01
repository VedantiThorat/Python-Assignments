import csv
file_name="data.csv"
with open(file_name):
    reader=csv.reader(file_name)
    row_count=0
    for row in reader:
    print(" Total number of roads in CSV file are",row count)