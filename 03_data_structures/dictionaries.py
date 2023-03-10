# Dictionaries

# Create simple dictionary
fruits = {'orange': 'orange', 'apple': 'red', 'pear': 'yellow', 'banana': 'yellow', 'kiwi': 'brown'}
print(fruits)

# Add new pair to dictionary
fruits['watermelon'] = 'green'
print(fruits)

# Convert list of tuples to dictionary using dict()
fruits = [('orange', 'orange'), ('apple', 'red'), ('pear', 'yellow'), ('banana', 'yellow'), ('kiwi', 'brown')]
print(dict(fruits))

# Using dict() to specify pairs using keyword arguments
fruits = dict(orange='orange', apple='red', pear='yellow', banana=1)
print(fruits)

