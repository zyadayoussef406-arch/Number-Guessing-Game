import random
secret_number = random.randint(1,100)
print("welcome to the number gussing game!")
print("guess a number between 1 and 100")

while True:
    guess = int (input("enter your guess:"))
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("correct! you guessed the number.")
        break