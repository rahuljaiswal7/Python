# num = int(input("Enter a Number: "))
# match num:
#     case _ if(num<0):
#         print("Negative Number")
#     case _ if(num>0 and num<=50):
#         print("Positive Number 0 To 50")
#     case _ if(num>50 and num<=100):
#         print("Positive Number 50 To 100")
#     case _:
#         print("Big number of 100")


Color  = input("Enter Color: ")
match Color:
    case _ if(Color=="Red"):
        print("Red Color")
    case _ if(Color=="Green"):
        print("Green Color")
    case _ if(Color=="Blue"):
        print("Blue Color")
    case _ if(Color=="Yellow"):
        print("Yellow Color")
    case _ if(Color=="Purple"):
        print("Purple Color")
    case _ if(Color=="Orange"):
        print("Orange Color")
    case _ if(Color=="Aqua"):
        print("Aqua Color")
    case _ :
        print("Your Color are not in my shop ")


