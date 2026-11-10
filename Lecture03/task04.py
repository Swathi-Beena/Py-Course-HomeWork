import random
number = random.randint(1,10)
guess = int(input("guess a number between 1 and 10 : "))
while guess != number:
    if guess > number:
        print("too high")
    else:
        print("too low")
    guess = int(input("guess again : "))
print("correct")