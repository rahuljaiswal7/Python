# Gussing Game
import random
magic_number = random.randint(0, 20)
guesses = -1
print("Welcome To Our Magic Show")
print("Please Guess The Number Between 0 and 20")
while guesses != magic_number:
    guesses = input("Guess The Number")
    if guesses== magic_number:
        print("Congrats You Won")
        break
    else:
        print("Sorry You Lose! Try Again")



