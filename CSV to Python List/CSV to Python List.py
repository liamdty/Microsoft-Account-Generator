#This is a tool to simply convert a profile spreadsheet to the format needed for the account generator
#Use the provided format in CSV.csv to provide desired profiles
import csv

with open('CSV.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)
