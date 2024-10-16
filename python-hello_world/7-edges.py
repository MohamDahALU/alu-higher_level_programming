#!/usr/bin/python3
word = "Holberton"
# why do I need to set them in variables? Still not doing it the "intended way"
[first, last, middle] = [word[:3], word[-2:], word[1:-1]]

print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[-2:]}")
print(f"Middle word: {word[1:-1]}")
