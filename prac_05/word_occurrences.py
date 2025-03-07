"""
CP1404/CP5632 Practical
Word Occurrence Counter
This program counts the occurrences of words in a user-provided string.
"""

# Get user input
text = input("Text: ").strip()

# Split the text into words and count occurrences
words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1  # Increment word count

# Sort words alphabetically
sorted_words = sorted(word_counts.keys())

# Find the longest word length for alignment
max_length = max(len(word) for word in sorted_words)

# Print the word counts with aligned numbers
for word in sorted_words:
    print(f"{word:{max_length}} : {word_counts[word]:>2}")