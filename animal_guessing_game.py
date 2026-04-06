import random
animal_list = ["cow","dog","goat","pig"]
attempt = 0
guess_animal = random.choice(animal_list)
print("Guess animal name")
while True:
    guess = input("Enter animal name : ").lower()
    attempt +=1
    if guess == guess_animal:
        print("Congratulations you are correct")
        print("It took ",attempt,"attempts for you to be correct")
        break
    elif guess != guess_animal:
        print("You are incorrect")
        print("Please try again")