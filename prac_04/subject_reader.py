"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)  # Display the processed data as a list of lists


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


main()
