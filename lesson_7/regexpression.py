import re

text = "The status is passed"
result = re.search("passed", text)
print(result)
print(result.group())
text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("passed", text2))
print(re.match("passed", text3))

print()
print(re.search("d.g", "dog"))
print(re.search("d.g", "dig"))
print(re.search("d.g", "dg"))

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))

print(re.search("Test$","Start is Test"))
print(re.search("Test$","Test Start is"))

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","green"))

print(re.search("[a-z]","Sofiia"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","sofiia"))
print(re.search("[A-Za-z]","sofiia"))
print()

print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))


print(re.search(r'\d',"Order #34"))
print(re.search(r'\w',"!!!Sofiia"))
print(re.search(r"\s","SofiiaQA 54"))

print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abc"))

print(re.search(r"colou?r", "color"))
print(re.search(r"colou?r", "colour"))
print(re.search(r"colou?r", "colouur"))
print(re.search(r"\d{3}", "13"))
print(re.search(r"\d{3}", "15666638"))
print(re.search(r'\d{2,4}', "123456"))
print(re.search(r'\d{3,4}', "323"))