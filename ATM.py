# MINI ATM
user_Id = "alex07"
password = "1234"
phone_No = "1234567890"
total_Balance = 10000

user_Input1 = input("Enter your UserId:")
user_Input2 = input("Enter your Password:")
if user_Input1 == user_Id and user_Input2 == password:
    print("✅Wow you are correct!")
    print("Hi There! 👋 Welcome To NVR ATM! 😊")
    while True:
        print("1. Check balance")
        print("2. Withdraw amount")
        print("3. Deposit amount")
        print("4. Change phone number")
        print("5. Change Password")
        print("6. Exit")
        choice = int(input("Choose Any One Option 1 to 6:"))
        if choice == 1:
            print("💰Your Balance is:",total_Balance)
        elif choice == 2:
            amount = int(input("Enter your Withdraw amount:"))
            if amount > total_Balance:
                print("❌Insufficient Balance")
            else:
             total_Balance = total_Balance - amount
            print("💰Your Total Balance is:",total_Balance)
        elif choice == 3:
            deposit_amount = int(input("Enter your Deposit amount:"))
            total_Balance = total_Balance + deposit_amount
            print("💰Your Balance is:",total_Balance)
        elif choice == 4:
            new_Number = input("Enter your New Number:")
            phone_No = new_Number
            print("✅Your Phone Number Has Been Changed:",phone_No)
        elif choice == 5:
            new_Password = input("Enter your New Password:")
            password = new_Password
            print("✅Your Password Has Been Changed:",password)
        elif choice == 6:
            print("👋Thank you for using our service! \n Goodbye")
            break
        else:
            print("❗Invalid Choice please choose 1 to 5")
else:
    print("❌ Incorrect ID or Password. Access Denied!")