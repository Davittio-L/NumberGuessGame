import random

print("I am thinking of a number between 1 & 10")

random_number = random.randint(1, 11)

for random_number in range(1,  7):
    print('Take a guess...')
    guess = int(input())

    if guess < random_number:
        print("Your guess was to low.")
    elif guess > random_number:
        print("Your guess was to high.")