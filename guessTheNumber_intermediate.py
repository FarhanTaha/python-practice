import random

def play_game():
    print("Welcome to the Guess the Number Game!")
    print("Choose a difficulty level:\n1. Easy (1-10, 5 attempts)\n2. Medium (1-20, 6 attempts)\n3. Hard (1-50, 8 attempts)")

    # Select difficulty
    difficulty = input("Enter 1, 2, or 3: ")
    if difficulty == "1":
        max_number, max_attempts = 10, 5
    elif difficulty == "2":
        max_number, max_attempts = 20, 6
    elif difficulty == "3":
        max_number, max_attempts = 50, 8
    else:
        print("Invalid choice, defaulting to Medium difficulty.")
        max_number, max_attempts = 20, 6

    secret_number = random.randint(1, max_number)
    print(f"I am thinking of a number between 1 and {max_number}. You have {max_attempts} attempts.")

    for guesses_taken in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {guesses_taken}/{max_attempts}. Take a guess: "))
                if 1 <= guess <= max_number:
                    break
                else:
                    print(f"Please enter a number between 1 and {max_number}.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed my number in {guesses_taken} attempts! 🎉")
            break
    else:
        print(f"Game Over! The correct number was {secret_number}.")

# Run the game
play_game()
