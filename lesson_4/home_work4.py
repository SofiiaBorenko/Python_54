
import csv
import json
from pathlib import Path


# 1.
def save_books(books):
    with open("books.txt", "w", encoding="utf-8") as file:
        for book in books:
            file.write(book + "\n")

books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "The Little Prince"
]

save_books(books)


# 2.

def read_products(filename):
    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)

        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")



# 3.
def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, ensure_ascii=False, indent=4)


# 4.
def create_logs_folder():
    logs_path = Path("logs")
    logs_path.mkdir(exist_ok=True)

    file_path = logs_path / "app.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Application started successfully!")


if __name__ == "__main__":
    read_products("products.csv.py")

    save_user("anna21", "anna@example.com", "Israel")

    create_logs_folder()
