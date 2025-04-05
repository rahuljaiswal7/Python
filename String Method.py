# Upper() Method
Str1 = "rahul jaiswal"
print(Str1.upper())

str2 ="Hello Rahul JaIswal "
print(str2.upper())

#Lower() Method
Str3 = "Hello Guys, HOW ARE YOU"
print(Str3.lower())

str4 = "HELLO GUYS, WHERE ARE GOING YOU WITHOUT MY PERMISSION"
print(str4.lower())

# rstrip() method
str5 = "Hello World!!!"
print(str5.rstrip("!"))

str6 = "!!!Hello World!!!"
print(str6.rstrip("!"))

# Replace() Method
str7 = "Hello World"
print(str7)
print(str7.replace("Hello World","Hello Guys"))

str8 = "Hello Boy Where Are Going You Without My Permission"
print(str8)
print(str8.replace("Hello Boy Where Are Going You Without My Permission", "Sir I have Also Permission"))

# Split()Method
str9 = "Hello Brother Please Eat Apple"
print(str9.split())

# Capitalize() Method
str10 ="introduction of javascript"
print(str10.capitalize())

str11 = "rahul jaiswal"
print(str11.capitalize())

# Center() Method
str12 = "Hello Rahul Jaiswal "
print(str12.center(50))

str13 = "Hello Brother, It is Center "
# print(str13)
print(str13.center(70))

# Count() Method
str14 = "Rahul Jaiswal !!! Ritik Jaiswal  !!! Abhishek Jaiswal !!! Rishabh Jaiswal !!! Rahul Jaiswal"
print(str14.count("Jaiswal"))

str15 = "Rahul Jaiswal !!! Ritik Jaiswal  !!! Abhishek Jaiswal !!! Rishabh Jaiswal !!! Rahul Jaiswal"
print(str15.count("Rahul"))


# Find() method
str16 = "Hello Guys, I Am Rahul Jaiswal From Bihar"
print(str16.find("Am"))

str17 = "Hello Guys, I Am Rahul Jaiswal From Bihar"
print(str17.find("Jaiswal"))

# index() Method
str18 = "Hello Brother"
print(str18.index("Brother"))

# Isalnum() method : Space between in string then return False
str19 = "Hello Dhoni Fan007"
print(str19.isalnum())

str20 ="07"
print(str20.isalnum())

str21 = "True07"
print(str21.isalnum())

#Isalpha() Method
str22 = "HelloBrother"
print(str22.isalpha())

str23 = "HelloBrother07"
print(str23.isalpha())

#Swapcase() Method
str24 = "rahul jaiswal"
print(str24.swapcase())

str25 = "RAHUL JAISWAL"
print(str25.swapcase())

# Startswith()Method
str26 = "Hello Boys, How are You"
print(str26.startswith("You"))

str27 = "Hello Boys, How are You"
print(str27.startswith("Hello"))

# Endswith() Method
str28 = "Hello Sir, I Am Good"
print(str28.endswith("Hello"))

str29 = "Hello Sir, I Am Good"
print(str29.endswith("Good"))

#title() Method
str30 = "hello guys, this is introduction of python"
print(str30.title())

str31 = "introduction of javascript"
print(str31.title())
