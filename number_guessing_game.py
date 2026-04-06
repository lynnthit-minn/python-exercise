import random
secret_number =random.randint(1,10)
guess = 0
attempt = 0
print("Guess a number between 1 to 10 ")
while guess != secret_number:
    guess = int(input("Enter your guess : "))
    attempt +=1
    if guess>secret_number:
        print("Too high")
    elif guess<secret_number:
        print("Too low")
    else:
        print("Your picked the correct number")
        print("You guessed in ",attempt, "attempts")