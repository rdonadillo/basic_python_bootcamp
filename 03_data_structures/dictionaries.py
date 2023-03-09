# Dictionaries

fruits = {'orange': 'orange', 'apple': 'red', 'pear': 'yellow', 'banana': 'yellow', 'kiwi': 'brown'}
print(fruits)

# Add new pair
fruits['watermelon'] = 'green'
print(fruits)

# Using dict() with a given list of tuple
fruits = [('orange', 'orange'), ('apple', 'red'), ('pear', 'yellow'), ('banana', 'yellow'), ('kiwi', 'brown')]
print(dict(fruits))

# specify pairs using keyword arguments
fruits = dict(orange='orange', apple='red', pear='yellow', banana=1)
print(fruits)

