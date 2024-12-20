with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#print (file_contents)

def count_characters(file_contents):
    """Counts the occurrences of each letter in a file."""
    # Convert the file contents to lowercase for accurate counting
    lower_contents = file_contents.lower()
    
    # Initialize counters for each letter
    letter_counts = {
        'a': 0, 'b': 0, 'c': 0,
        'd': 0, 'e': 0, 'f': 0,
        'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0,
        'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0
    }
    
    # Count the occurrences of each letter
    for char in lower_contents:
        if char.isalpha():
            letter_counts[char] += 1
    
    return letter_counts








#--- Begin report of books/frankenstein.txt ---
print ("--- Begin report of books/frankenstein.txt ---")
words = len(file_contents.split())    
print (f"word count: {words}")
characters = len(file_contents.lower())
print (f"character count: {characters}")

char_counts = count_characters(file_contents)
for char, count in char_counts.items():
    print(f"The '{char}' characater was found {count} times")



