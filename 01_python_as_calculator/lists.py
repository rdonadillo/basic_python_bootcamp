# Lists

# Number of compound data types, used to group together  other values.
items = [1, 2, 3, 5, 8, 13]
print(items)
print(items[0]) # First index
print(items[-1]) # Shortcut to Last index
print(items[-3])

# Support operations like concatenation
items = items + [21, 34, 55]
print(items)

# Mutable type
items = [1, 2, 3, 5, 8, 13]
items[4] = 10
print(items)

# Add new items by using append()
items = [1, 2, 3, 5, 8, 13]
items.append(21)
print(items)

# Assignment to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

# Nested lists
a = ['a', 'b', 'c']
b = [1, 2 ,3]
n = [a, b]
print(n)
print(n[0])
print(n[0][2])