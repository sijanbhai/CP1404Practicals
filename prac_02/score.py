import random

def get_score_result(score):
    """Determine the score category and return the result as a string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to get user input, process the score, and print the result."""
    # User input for score
    score = float(input("Enter score: "))
    result = get_score_result(score)  # Call the function to get the result
    print(result)  # Print the result separately

    # Generate a random score and print its result
    random_score = random.randint(0, 100)
    print(f"\nRandomly generated score: {random_score}")
    print(get_score_result(random_score))  # Reusing the function

# Call the main function
if __name__ == "__main__":
    main()
