import random

print("Number Guessing Game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("enter your guess:- "))

    if guess == number:
        print("Congratulations you won!!!")
        break

    elif guess < number:
        print("your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: guess a number lower than", guess)

    chances == 1

if not chances < 5:
    print("you lose!!! the number is", number)
