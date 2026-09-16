# Task 1. Clean a Name

def clean_name(name):
    return name.strip().title()


print(clean_name("  anna smith  "))
print(clean_name("DAVID COHEN"))



# Task 2. Normalize an Email

def normalize_email(email):
    return email.strip().lower()

print(normalize_email("  Anna.Smith@Example.COM  "))



# Task 3. Check a File Name

def is_python_file(filename):
    return filename.lower().endswith(".py")


print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))



# Task 4. Replace Words

def fix_message(message):
    return message.replace("bad", "good")

message = "bad weather, bad mood"
result = fix_message(message)
print(result)
print(message)



# Task 5. Count a Letter

def count_letter(text, letter):
    return text.lower().count(letter.lower())

print(count_letter("Programming", "g"))
print(count_letter("Mississippi", "I"))



# Task 6. Create a Short Login

def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return first_name + "." + last_name

print(create_login("  Anna ", " SMITH "))


# Bonus 1. Split Full Name

def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Anna Smith  "))
print(split_name("David Cohen"))



# Bonus 2. Simple Password Check

def check_password(password):
    return len(password) >= 8 and " " not in password and not password.isalpha()

print(check_password("python123"))
print(check_password("python"))
print(check_password("python 123"))
