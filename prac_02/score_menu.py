import random


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 (inclusive)."""
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


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


def show_stars(score):
    """Print as many stars as the score value."""
    print("*" * int(score))


def display_menu():
    """Display the menu options."""
    print("\nMENU")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    """Main function to run the program using a menu system."""
    print("Welcome to the Score Program!")

    # Get an initial valid score
    score = get_valid_score()

    # Display menu and get user choice
    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Score: {score}, Result: {get_score_result(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice! Please select a valid option.")

        # Show menu again
        display_menu()
        choice = input(">>> ").upper()

    print("Goodbye! Thanks for using the program.")


# Call the main function
if __name__ == "__main__":
    main()
