def determine_score_category(score):
    """Determine the score category based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to get user input and print the score category."""
    score = float(input("Enter score: "))
    result = determine_score_category(score)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
