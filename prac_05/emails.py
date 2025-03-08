"""
CP1404/CP5632 Practical
User Email and Name Storage Program
This program collects users' emails and extracts their names to store them in a dictionary.
Emails serve as unique keys, while names are the values.
"""

# Dictionary to store email-to-name mapping
EMAIL_TO_NAME = {}


# Function to extract a name from an email
def get_name_from_email(email):
    """Extracts a guessed name from an email address."""
    name_part = email.split("@")[0]  # Get the part before '@'
    name_parts = name_part.split(".")  # Split by '.' or '_'
    guessed_name = " ".join(name_parts).title()  # Capitalize each word
    return guessed_name


# Get user input and store emails and names
while True:
    email = input("Enter your email (or press Enter to finish): ").strip()
    if not email:
        break  # Stop if the user enters nothing

    # Suggest a name based on the email
    guessed_name = get_name_from_email(email)
    confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

    # Allow user to correct the name
    name = guessed_name if confirmation in ("", "y", "yes") else input("Enter your name: ").title()

    EMAIL_TO_NAME[email] = name  # Store in dictionary

# Print stored emails and names
print("\nStored emails and names:")
for email, name in EMAIL_TO_NAME.items():
    print(f"{name} ({email})")
