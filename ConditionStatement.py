# Age = int(input("Enter Age : "))
# print("Your Age is", Age)
# if(Age >= 18):
#     print("You Can Drive")
# else:
#     print("Sorry Sir You Can Not Drive")

# age = int(input("Enter Age : "))
# print("Your Age is :", age)
# if(age>=18):
#     print("You Are Eligible For Voting ")
# else:
#     print("Sorry Sir You Are Not Eligible For Voting ")


# If elif Else

# Num = int(input("Enter Number : "))
# print("Your Number Is:", Num)
# if(Num>=18 and Num<=20):
#     print("You Can Play U19")
# elif(Num>=21 and Num<=35):
#     print("You Can Play International Cricket")
# elif(Num>35):
#     print("You Can Take Retirement From Cricket")
# else:
#     print("You Can Not play U19 Because You are Below 18")


# Compare Number

# Num1 = int(input("Enter Number : "))
# Num2 = int(input("Enter Number : "))
# if(Num1>Num2):
#     print("NUMBER1 GRATER THAN NUMBER2 ")
# elif(Num1<Num2):
#     print("NUMBER1 IS SMALLER THAN NUMBER2")
# else:
#     print("BOTH NUMBER ARE EQUAL")


#GRADING SYSTEM

# Mark = int(input("Enter Mark : "))
# if(Mark>=90):
#      print("GRADE A")
# elif(Mark>=80):
#     print("GRADE B")
# elif(Mark>=70):
#     print("GRADE C")
# elif(Mark>=60):
#     print("GRADE D")
# elif(Mark>=50):
#     print("GRADE E")
# else:
#     print("Fail")


# Nested If

AGE = int(input("Enter Your Age : "))
if(AGE>=18):
    print("You Can Eligible For Voting")
    if(AGE>=21):
        print("You Can Eligible For Driving License")
    else:
        print("You Can Not Eligible For Driving License")
else:
    print("You Can Not Eligible For Voting Or Driving License")

