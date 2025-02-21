"""
CP1404/CP5632 - Practical
Get an integer from the user and does not crash when a non-number is entered.
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop if input is valid
    except ValueError:  # Catch ValueError when conversion to int fails
        print("Please enter a valid integer.")
print("Valid result is:", result)
