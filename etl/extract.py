import csv


def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
# This change is to test the Feature Extract Step Branch 
# This is the second change to test the Feature Extract Step Branch 
    return rows