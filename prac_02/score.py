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
    score = float(input("Enter score: "))
    result = get_score_result(score)  # Call the function to get the result
    print(result)  # Print the result separately

# Call the main function
if __name__ == "__main__":
    main()
