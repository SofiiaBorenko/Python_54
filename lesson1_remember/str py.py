s = "cat"
s = s.upper()
print(s)

s1 ='Hello'
s2 ="Hello"
s3 ="""Line one 
Line Two """
print(s1)
print(s2)
print(s3)

s = "Hello my group!"
print(len(s))
print(s[0])
print(s[4])
print(s[14])
print(s[-1])
print(s[100])

s1 = "P y t h o n "
#ind  0 1 2 3 4 5 -> index of last element = len()-1 or -1

#slicing -> my_string[start:end:step]
text = "automation"
       #0123456789
print(s1[2:6])
print(next[:4])
print(next[4:])
print(next[:])
print(next[::2])
print(text[::-1])
print(text[5:100])

name = "Mariia"
last_name="Ivanova"
age = 25
print(name+" "+last_name+ "-" + str(age))
print(f"Hi me name is {name} and my lat name is {last_name}and my age {age}")

raw = "Automation QA"
print(raw.upper())
print(raw.lower())
#strip()
print(raw.strip().upper())

#split()/join():

cvs_line = "Login,Cart,Checkout,Mama,Papa"
parts = cvs_line.split(",")
print(parts)
print(" - ".join(parts))
msg = "Test failed: element not found"






