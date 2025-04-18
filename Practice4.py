# Loop problem
# odd number
# numbers = [1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     if num % 2 != 0:
#         print(num)


# Create a loop to print a pattern
# for i in range(1,11):
#     print("*" * i)

# for i in range(100):
#     if i == 10:
#         break
#     print("*" * i)

# while loop
# Print even numbers from 2 to 20 using a while loop
# i = 2
# while i <= 20:
#     print(i)
#     i = i + 2


user_id = "alex07"
password = 12345

take_user = input("Please Enter Your User Id: ")
pass_user = int(input("Please Enter Your Password: "))

if take_user == user_id or pass_user == password:
     print("Welcome ATM ")
else:
     print("Invailid !!")

