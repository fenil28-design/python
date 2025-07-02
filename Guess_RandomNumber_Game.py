#Guess the random  number game 

import random
print("Guess the number between 1 to 10")
guess_number=int(input("Enter your Guess number between 1 to 10:"))
number=random.randint(1,10)
if guess_number==number:
    print("congratulations You Won The Game ")
     
else:
    print(" oops! Sorry You Lost The Game")
    print("The number was:", number)
