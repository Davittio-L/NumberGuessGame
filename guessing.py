import random

choice = input("Please choose a difficulty: Easy, Medium, Hard: ")

if choice == lowercase("easy"):

    print("I am thinking of a number between 1 & 10")

    random_number = random.randint(1, 11)

    for guessTaken in range(1,  7):
        print('Take a guess...')
        guess = int(input())

        if guess < random_number:
            print("Your guess was to low.")
        elif guess > random_number:
            print("Your guess was to high.")
        else:
            break

    if guess == random_number:
        print('Good job you guessed the correct number in ' + str(guessTaken) + 'guesses!')
    else:
        print('You ran out of guesses! The number was ' + str(random_number))