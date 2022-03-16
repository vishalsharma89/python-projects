import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        count = count+1
        if guess < random_number:
            print("Guess is to Low")
        elif guess > random_number:
            print("Guess is to High")

    print(
        f'Congrats You Have Guessed the number {random_number} correctly!! in {count} counts')


guess(100)
