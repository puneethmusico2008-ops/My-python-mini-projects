
'''
In this script we will be knoing about the number guessing game.

The program generates a random number between 1 and 1000, and the user has to guess the number.
 The program provides feedback on whether the user's guess is too high, too low, or correct.
 The game continues until the user guesses the correct number.
 '''


num = int(input("Guess a number between 1 and 1000: "))
number_to_guess = 168
attempts = 0
while attempts < 6:
    if num < 1 or num > 1000:
        print("Please enter a number between 1 and 1000.")
    else:
        attempts += 1
        if num == number_to_guess:
            print("Congratulations! You guessed the correct number:", number_to_guess)
            break
        elif num < number_to_guess:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
    if attempts < 5:
        num = int(input("Guess a number between 1 and 1000: "))
    else:
        print("Sorry, you've used all your attempts. The correct number was:", number_to_guess)

while num != number_to_guess:
    if num < number_to_guess:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    num = int(input("Guess a number between 1 and 1000: "))

   