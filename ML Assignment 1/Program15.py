#Write a program that reads data from a CSV file and prints it to the console.

import csv

with open("Samplecsv.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)