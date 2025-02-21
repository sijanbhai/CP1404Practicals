"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent.
"""
import random

# Constants for price simulation
MAX_INCREASE = 0.10  # 10% increase
MAX_DECREASE = 0.05  # 5% decrease
MIN_PRICE = 0.01  # Minimum price of $0.01
MAX_PRICE = 1000.00  # Maximum price of $1000
INITIAL_PRICE = 10.0  # Starting price
FILENAME = "stock_prices.txt"  # File to write output

# Initialize the price and day counter
price = INITIAL_PRICE
day = 0

# Open file using a context manager
with open(FILENAME, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)

    # Simulation loop
    while MIN_PRICE <= price <= MAX_PRICE:
        day += 1  # Increment the day counter
        price_change = 0

        # Determine price change direction (increase or decrease)
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)  # Increase
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)  # Decrease

        # Update and round the price
        price = round(price * (1 + price_change), 2)

        # Write the day's price to the file
        print(f"On day {day} price is: ${price:,.2f}", file=out_file)

    # Final price output after the loop ends
    print(f"Final price after {day} days: ${price:,.2f}", file=out_file)
