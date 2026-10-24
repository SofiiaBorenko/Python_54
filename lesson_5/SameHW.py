import csv
from pathlib import Path


def save_shopping_list(items):
    with open("shopping_list.txt","w",encoding="utf-8") as file:
        for item in items:
            file.write(item+"\n")

items = [
                "Milk",
                "Bread",
                "Apples",
                "Coffee"
]
save_shopping_list(items)

with open("shopping_list.txt","r",encoding="utf-8") as file:
    print(file.read())

def read_students(filename):
    with open("students.csv","r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")

read_students("students.csv")

def create_reports_folder():
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    results_file = reports_dir/"result.txt"
    with open(results_file,"w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")