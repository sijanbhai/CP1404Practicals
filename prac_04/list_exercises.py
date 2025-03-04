"""
CP1404/CP5632 Practical
List Exercises
"""
def main():
    """Prompt the user for 5 numbers, store them in a list, and display statistics."""
    numbers = []  # Initialize an empty list

    for i in range(5):
        number = float(input(f"Number: "))  # Get user input
        numbers.append(number)  # Add the number to the list

    print("\nThe first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


"""Check if a user is authorized."""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")  # Get user input

if username in usernames:  # Check if username is in the list
        print("Access granted")
else:
        print("Access denied")
main()

