import csv

with open("data2.csv",mode='r', encoding="utf-8") as f:
    read=csv.reader(f)
    for row in read:
        print(row[0].split(";"))
