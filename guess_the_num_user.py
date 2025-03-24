#project 3: Guess the number Game by User
#1 to 100 Numbers

import random
print("Guess the number between 1 tp 100")
number = random.randint(1, 100)
#welcome Message
print("Welcome to the Game!!!")
# print("Guessing number.......")
# print("loading...... ,please wait!!!")
    
while True:
    guess = int(input("Enter another number: "))
    if guess < number:
        print("Too smaller Number!!! Guess another..")
    elif guess > number:
        print("Too Bigger Number!!! Guess another..")
    else:
        print("Yahooo!!!! You got the correct number ")
        break