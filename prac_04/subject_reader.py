"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load data and display subject details."""
    data = load_data()
    display_subject_details(data)  # Call the new function to display details


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data = []  # Initialize an empty list to store processed data
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline characters
            parts = line.split(',')  # Split into components
            parts[2] = int(parts[2])  # Convert number of students to an integer
            data.append(parts)  # Add the processed line (list) to the main list
    return data  # Return the list of lists


def display_subject_details(data):
    """Display subject details in a readable format."""
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer} and has {students} students")


main()
