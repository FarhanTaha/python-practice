# Example code: Using break and continue in a for loop
for num in range(1, 10):  # Looping through numbers 1 to 9
    if num == 5:
        print("Encountered 5, breaking the loop.")
        break  # Exit the loop when num is 5
    elif num % 2 == 0:
        print(f"{num} is even, skipping this iteration.")
        continue  # Skip to the next iteration for even numbers
    print(f"Processing number: {num}")