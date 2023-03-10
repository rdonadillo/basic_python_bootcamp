# Lists

# Number of compound data types, used to group together  other values.
# Create a simple list
items = [1, 2, 3, 5, 8, 13]
print(items)
print(items[0]) # First index
print(items[-1]) # Shortcut to Last index
print(items[-3])

# Support operations like concatenation
# Create a list that concatenates with other list
items = items + [21, 34, 55]
print(items)

# Mutable type
# Create a list and change the value of any of the index
items = [1, 2, 3, 5, 8, 13]
items[4] = 10
print(items)

# Add new items by using append()
items = [1, 2, 3, 5, 8, 13]
items.append(21)
print(items)

# Assignment to slices
# Create a list and assign value by slicing the list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

# Nested lists
# Create a list of lists
a = ['a', 'b', 'c']
b = [1, 2 ,3]
n = [a, b]
print(n)
print(n[0])
print(n[0][2])