import random
from termcolor import colored
secret_number = random.randint(1, 99)

print("Guess number between 1 and 99.")

while True:
    try:
        user_guess = int(input("Enter 1-99 or type '999' to exit: "))
    except: 
        print("Please enter valid number")
        continue
    if user_guess == 999:
        print("Goodbye! The number was", secret_number)
        break
    elif user_guess < 1 or user_guess > 99:
        print("Please enter a number between 1 and 99.")
    elif user_guess < secret_number:
        print(colored("Not correct.",'red') + "The number is bigger.")
    elif user_guess > secret_number:
        print(colored("Not correct.",'red') + "The number is smaller.")
    else:
        print("Congratulations! You guessed the correct number!!!")            
        break
