import tkinter as tk
import random

# Function to start the game
def start_game():
    # Get selected difficulty
    difficulty = difficulty_var.get()
    if difficulty == "1":
        max_number, max_attempts = 10, 5
    elif difficulty == "2":
        max_number, max_attempts = 20, 6
    elif difficulty == "3":
        max_number, max_attempts = 50, 8
    else:
        max_number, max_attempts = 20, 6

    # Initialize secret number and attempts
    secret_number = random.randint(1, max_number)
    attempts_left = max_attempts

    # Update the UI elements
    message_label.config(text=f"Guess a number between 1 and {max_number}. You have {attempts_left} attempts.")
    guess_button.config(state=tk.NORMAL)
    guess_entry.config(state=tk.NORMAL)
    play_again_button.config(state=tk.DISABLED)
    
    # Function to process the guess
    def check_guess():
        nonlocal attempts_left
        try:
            guess = int(guess_entry.get())
            if guess < 1 or guess > max_number:
                result_label.config(text=f"Please enter a number between 1 and {max_number}.")
                return
        except ValueError:
            result_label.config(text="Invalid input! Please enter a number.")
            return

        attempts_left -= 1
        
        if guess < secret_number:
            result_label.config(text=f"Too low! {attempts_left} attempts left.")
        elif guess > secret_number:
            result_label.config(text=f"Too high! {attempts_left} attempts left.")
        else:
            result_label.config(text=f"🎉 Congratulations! You guessed my number! 🎉")
            guess_button.config(state=tk.DISABLED)
            play_again_button.config(state=tk.NORMAL)
            return
        
        if attempts_left == 0:
            result_label.config(text=f"Game Over! The correct number was {secret_number}.")
            guess_button.config(state=tk.DISABLED)
            play_again_button.config(state=tk.NORMAL)
    
    guess_button.config(command=check_guess)

# Function to reset the game
def reset_game():
    difficulty_var.set("2")
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    start_game()

# Set up the main window
root = tk.Tk()
root.title("Guess the Number Game")

# Difficulty options
difficulty_var = tk.StringVar(value="2")  # Default to medium
difficulty_label = tk.Label(root, text="Choose a difficulty level:")
difficulty_label.pack()

easy_radio = tk.Radiobutton(root, text="Easy (1-10, 5 attempts)", variable=difficulty_var, value="1")
easy_radio.pack()
medium_radio = tk.Radiobutton(root, text="Medium (1-20, 6 attempts)", variable=difficulty_var, value="2")
medium_radio.pack()
hard_radio = tk.Radiobutton(root, text="Hard (1-50, 8 attempts)", variable=difficulty_var, value="3")
hard_radio.pack()

# Labels and entry for game interaction
message_label = tk.Label(root, text="Welcome to the Guess the Number Game!")
message_label.pack()

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

# Button to submit guess
guess_button = tk.Button(root, text="Guess", state=tk.DISABLED)
guess_button.pack()

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack()

# Button to start a new game
play_again_button = tk.Button(root, text="Play Again", command=reset_game, state=tk.DISABLED)
play_again_button.pack()

# Start the game when the application runs
start_game_button = tk.Button(root, text="Start Game", command=start_game)
start_game_button.pack()

# Run the app
root.mainloop()
