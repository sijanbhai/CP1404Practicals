import random

# Constants for the lottery number range and pick size
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Generate quick pick lottery numbers."""
    num_picks = int(input("How many quick picks? "))  # Get user input

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print_formatted_pick(quick_pick)


def generate_quick_pick():
    """Generate a single quick pick of 6 unique random numbers."""
    numbers = []  # List to store the unique numbers

    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)  # Generate a random number
        if num not in numbers:  # Ensure no duplicates
            numbers.append(num)

    numbers.sort()  # Sort the numbers in ascending order
    return numbers


def print_formatted_pick(pick):
    """Print the quick pick with proper formatting."""
    print(" ".join(f"{num:2}" for num in pick))  # Ensures two-space alignment


main()
