"""
CP1404/CP5632 Practical
Hexadecimal Colour Code Lookup
This program allows users to look up the hexadecimal colour code for a given colour name.
"""

# Dictionary containing color names and their hexadecimal codes
COLOUR_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "BlueViolet": "#8A2BE2"
}

# Print available colors
print("Available colours:")
for colour in COLOUR_TO_HEX:
    print(colour)

# User input loop
colour_name = input("\nEnter a colour name to get its hexadecimal code (or press Enter to quit): ").strip()
while colour_name:
    colour_name = colour_name.replace(" ", "").title()  # Normalize input for case insensitivity
    if colour_name in COLOUR_TO_HEX:
        print(f"{colour_name} has the hex code {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name. Please try again.")
    colour_name = input("\nEnter another colour name (or press Enter to quit): ").strip()

print("Goodbye!")
