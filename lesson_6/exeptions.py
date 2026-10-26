# with open("user.json","r",encoding="utf-8") as file:
#     print(file.read())


# print("Hello World")
# result = 10 / 0
# print(result)
# print("Bye World")

# def div_int(a,b):
#     return a/b
# print("start program")
# result = div_int(10,0)
# print(result)
# print("end program")

#try/except

# print("Hello World")
# try:
#     result = 10/0
#     print(result)
# except Exception as e:
#     print("An error occured: e")
# print("BY")

# try/except

# print("Hello World")
# try:
#     result = 10 / 0
#     print(result)
# except Exception as e:
#     print("An error occurred: ", e)
# # print("BY")
# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("Result: ", result)
# except ValueError:
#     print("Error: Please enter a valid number")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Kris"))
print(is_number(None))