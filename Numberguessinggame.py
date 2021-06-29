import random

print("Number Guessing Game")
chances = 0

name = input("What's your name?")
name = print(name)

num = random.randint(1,10)

while chances <5 :
    guess = int(input("Guess a number between 1 and 10"))
    print(guess)
    
    if guess < num:
        print(name,",your guess was too small")
        chances += 1
    elif guess == num:
        print(name,",your guess is right!!! You won /n Press Ctrl+C to try again")

    else: 
        print(name,",your guess was too big")
        chances += 1

if not chances < 5 :
    print(name,"You Lose")