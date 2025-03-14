"""
CP1404/CP5632 Practical
User Email and Name Storage Program
Estimated time: 15 minutes
Actual time: 25 minutes
This program collects users' emails and extracts their names to store them in a dictionary.
Emails serve as unique keys, while names are the values.
"""

# Dictionary to store email-to-name mapping
EMAIL_TO_NAME = {}

def get_name_from_email(email):
    """Extracts a guessed name from an email address."""
    name_part = email.split("@")[0]  # Get the part before '@'
    name_parts = name_part.replace(".", " ").replace("_", " ").split()  # Handle different separators
    return " ".join(name_parts).title()  # Capitalize each word and return

def main():
    """Main function to get emails and store names."""
    while True:
        email = input("Enter your email (or press Enter to finish): ").strip()
        if email == "":
            break  # Stop if the user enters nothing

        # Suggest a name based on the email
        guessed_name = get_name_from_email(email)
        confirmation = input(f"Is your name {guessed_name}? [Y/n] ").strip().lower()

        # Allow user to correct the name only if they explicitly say "n" or "no"
        if confirmation == "n" or confirmation == "no":
            name = input("Enter your name: ").title()
        else:
            name = guessed_name  # Default to guessed name if Enter is pressed or "y" is entered

        EMAIL_TO_NAME[email] = name  # Store in dictionary

    # Print stored emails and names
    print("\nStored emails and names:")
    for email, name in EMAIL_TO_NAME.items():
        print(f"{name} ({email})")

# Run the program
if __name__ == "__main__":
    main()