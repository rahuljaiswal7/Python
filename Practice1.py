# Leap Year or Not
# year = int(input("Enter Year: "))
# if(year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# # Check character upper or Lower
# chracter = input("Enter Character: ")
# if chracter.isupper():
#     print("Upper Character")
# elif chracter.islower():
#     print("Lower Character")
# else:
#     print("Not Latter")

# calculate salary with Bonus
salary = int(input("Enter Salary: "))
exprince = float(input("Enter Exprince: "))
if(salary>=15):
    bonus = salary * 0.20
else:
    bonus = salary * 0.10
print("Your Bonus is:",bonus)
total_money = salary + bonus
print("Your Total Salary is:", total_money)

