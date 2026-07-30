# This is a guess the number game.

# import random
# secret_number = random.randint(1, 20)
# print("I am thinking of a number between 1 and 20. Can you guess it in 6 guesses?")
# guesses_taken = 0
# guesses_left = 6
# while guesses_taken < 6 or guesses_left > 0:
#
#     # Ask the player to guess 6 times.
#     for guesses_taken in range(1, 7):
#         print("Take a guess.")
#         guess = int(input("> "))
#         guesses_left -= 1
#         if guess < secret_number or guess > secret_number:
#            print("Your guess is too low. You have " + str(guesses_left) +  " guesses left!")
#         elif guess > secret_number or guesses_left > 0:
#             print ("Your guess is too high. You have "  + str(guesses_left) +  " guesses left!")
#         else:
#             break # This condition is the correct guess!
# if guess == secret_number:
#     print("Good job! You got it in " + str(guesses_taken) + " guesses!")
# else:
#     print("The number was " + str(secret_number))

import random

# Setup the game
secret_number = random.randint(1, 20)
tries_left = 6

print("I am thinking of a number between 1 and 20.")

while tries_left > 0:
    # Alert the user of their remaining attempts
    print(f"\nYou have {tries_left} tries left.")

    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print(f"Classic! You guessed it. The number was {secret_number}!")
        break  # Stops the loop immediately

    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    # Decrease tries by 1 for the next loop iteration
    tries_left -= 1

# This runs only if the loop finishes naturally (tries run out)
if tries_left == 0:
    print(f"\nGame over! You ran out of tries. The number was {secret_number}.")