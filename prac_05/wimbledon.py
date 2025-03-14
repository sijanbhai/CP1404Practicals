"""
CP1404/CP5632 Practical
Wimbledon Champions Data Processor
Estimated time: 20 minutes
Actual time: 32 minutes

This program reads the Wimbledon champions data from a CSV file,
counts how many times each player has won, and lists the unique countries
that have produced winners.
"""

import csv

def read_wimbledon_data(filename):
    """Read the Wimbledon CSV file and return a list of records."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        return list(reader)

def process_winners(data):
    """Process the data to count wins per champion and store unique countries."""
    champions_dict = {}  # Dictionary to store player names and their win count
    countries_set = set()  # Set to store unique winning countries

    for row in data:
        country = row[1]
        champion = row[2]

        champions_dict[champion] = champions_dict.get(champion, 0) + 1
        countries_set.add(country)  # Store unique countries

    return champions_dict, countries_set

def display_results(champions_dict, countries_set):
    """Display the processed results: champion wins and sorted country list."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions_dict.items()):
        print(f"{champion} {wins}")

    # Sort countries alphabetically and format them in a single string
    sorted_countries = sorted(countries_set)
    print("\nThese", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def main():
    """Main function to run the program."""
    filename = "wimbledon.csv"  # Ensure this file is in the same directory
    data = read_wimbledon_data(filename)
    champions_dict, countries_set = process_winners(data)
    display_results(champions_dict, countries_set)

# Run the program
if __name__ == "__main__":
    main()
