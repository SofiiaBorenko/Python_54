
import re


# 1
def is_positive_less_than_300(value):
    return bool(re.fullmatch(r"[1-9]\d{0,1}|[12]\d{2}", value))


# 2
def is_number_from_1_to_255(value):
    return bool(re.fullmatch(r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])", value))


# 3
def is_israel_mobile(phone):
    pattern = r"(?:05\d{8}|05\d-\d{7}|\+9725\d-\d{3}-\d{4}|05\d-\d{2}-\d{2}-\d{3})"
    return bool(re.fullmatch(pattern, phone))


# 4
def is_valid_time(time):
    return bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", time))


# 5
def is_israel_car_number(number):
    pattern = r"(?:\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})"
    return bool(re.fullmatch(pattern, number))


print("Task 1:")
for value in ["1", "15", "99", "100", "299", "0", "300", "-5", "3.14", "Abc"]:
    print(value, "->", is_positive_less_than_300(value))

print("\nTask 2:")
for value in ["1", "25", "100", "255", "0", "256", "025", "-1", "2.5"]:
    print(value, "->", is_number_from_1_to_255(value))

print("\nTask 3:")
for phone in [
    "0541234567",
    "054-1234567",
    "+97254-123-4567",
    "058-12-34-567",
    "54-1234567",
    "054--12-4567",
    "+972054-123-4567",
    "97254-123-4567"
]:
    print(phone, "->", is_israel_mobile(phone))

print("\nTask 4:")
for time in ["00:00", "09:30", "14:45", "23:59", "24:00", "12:60", "8:30", "123:45", "12-30"]:
    print(time, "->", is_valid_time(time))

print("\nTask 5:")
for number in [
    "12-345-67",
    "99-999-99",
    "123-45-678",
    "456-78-901",
    "12345678",
    "12:345:67",
    "1-234-56",
    "1234-56-78"
]:
    print(number, "->", is_israel_car_number(number))
