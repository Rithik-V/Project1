import random

top_of_the_range = input("Type a number: ")

try:
    top_of_the_range = int(top_of_the_range)

    if top_of_the_range <= 0:
        print('Please type a number more than 0 next time.')
        quit()
except Exception:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_the_range)
no_of_guesses = 0

while True:
    no_of_guesses += 1
    guess = input("Make a guess: ")
    try:
        guess = int(guess)
    except Exception:
        print("Please type a number next time,you did'nt type a number this time!")
        continue

    if guess == random_number:
        print("You got it!")
        break
    elif guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", no_of_guesses, "guesses")
