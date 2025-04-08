# Q1 : Write a program to check whether a number is negative, positive or zero.
# num1 = int(input("Enter the first number: "))
# if(num1<0):
#     print("Negative Number")
# elif(num1>0):
#     print("Positive Number")
# else:
#     print("Zero")

# Q2 : Write a program to check whether a character is vowel or not.
# char = input("Enter the character: ")
# if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
#     print("Your Character Is Vowel")
# else:
#     print("Your Character Is Not Vowel")

# Q3 : Write a program to assign grades according to the given marks:-(85 to 100  : A Grade),(70 to 85   : B Grade),(60 to 70   : C Grade),(50 to 60   : D Grade),(<50        : Fail)
# Num = int(input("Hello Guys Please Enter Your Mark For Grading: "))
# if(Num>85 and Num<=100):
#     print("Your Grade is A")
# elif(Num>70 and Num<=85):
#     print("Your Grade is B")
# elif(Num>60 and Num<=70):
#     print("Your Grade is C")
# elif(Num>50 and Num<=60):
#     print("Your Grade is D")
# elif(Num>40 and Num<=50):
#     print("Fail")
# else:
#     print("Guys Please Enter Valid Marks")
#

# Q4. : Write a program to check weather a triangle is isosceles , equilateral or not.
# side1 = int(input("Enter the side 1: "))
# side2 = int(input("Enter the side 2: "))
# side3 = int(input("Enter the side 3: "))
# # rule bnate hai
# if side1+side2>side3 and side1+side2>side3 and side1+side3>side2:
# # check krte ab
#     if side1 == side2 == side3:
#         print("It is an Equilateral Triangle.")
# # 2 barabar hai ki nhi ye check krte hai
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print("It is an Isosceles Triangle.")
#     else:
#         print("It is not an Equilateral or Isosceles Triangle.")
# else:
#     print("Kya Bhai Tum Sachme Tringle ke Bare Me Hi Puchh Rahe Ho N.")


# Write a program to check whether an year is century year or not.
# year = int(input("Enter Year: "))
# if year % 100 == 0:
#     print("yes it is century year")
# else:
#     print("no it is century year")

# Q6. Write a program to input two numbers and check whether second number is multiple of first number or not.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 %num2 == 0:
#     print("Second Number is Multiple of First Number")
# else:
#     print("Second Number is Not Multiple of First Number")


# Q7. Write a program to convert an upper case character into lower case if it is in upper case.
char = input("Enter any character: ")
if char.isupper():
    print("lower Case:",char.lower())
elif char.islower():
    print("upper Case:",char.upper())
else:
    print("Enter a character only")

# Q8. Write a program to provide the following options to the user who is using the console in the banking system.
# This console should be available to the user if he enters correct id and password.
# 	1. check balance
# 	2. Withdraw amount
# 	3. deposit amount
# 	4. change phone number
# 	5. change password

user_Id = "alex07"
password = "1234"
phone_No = "1234567890"
total_Balance = 10000

user_Input1 = input("Enter your UserId:")
user_Input2 = input("Enter your Password:")
if user_Input1 == user_Id and user_Input2 == password:
    print("Wow you are correct!")
    print("1. Check balance")
    print("2. Withdraw amount")
    print("3. Deposit amount")
    print("4. Change phone number")
    print("5. Change Password")
    choice = int(input("Choose Any One Option 1 to 5:"))
    if choice == 1:
        print("Your Balance is:",total_Balance)
    elif choice == 2:
        amount = int(input("Enter your Withdraw amount:"))
        if amount > total_Balance:
            print("Insufficient Balance")
        else:
            total_Balance = total_Balance - amount
            print("Your Total Balance is:",total_Balance)
    elif choice == 3:
        deposit_amount = int(input("Enter your Deposit amount:"))
        total_Balance = total_Balance + deposit_amount
        print("Your Balance is:",total_Balance)
    elif choice == 4:
        new_Number = input("Enter your New Number:")
        phone_No = new_Number
        print("Your Phone Number Has Been Changed:",phone_No)
    elif choice == 5:
        new_Password = input("Enter your New Password:")
        password = new_Password
        print("Your Password Has Been Changed:",password)
    else:
        print("Invalid Choice please choose 1 to 5")
    print("Thank you for using our service!")
else:
    print("Incorrect ID or Password. Access Denied!")



