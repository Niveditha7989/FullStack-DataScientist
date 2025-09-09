'''14. Problem: Count how many times each character appears in a string.'''


string = "hello world"
counts = {}

for char in string:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1

for char in counts:
    print(char, ":", counts[char])
