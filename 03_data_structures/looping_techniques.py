# Looping Techniques

# Use items() method to retrieve the key and value when looping through dictionaries
fruits = {'orange': 'orange', 'apple': 'red', 'pear': 'yellow', 'banana': 'yellow', 'kiwi': 'brown'}
for fruit, color in fruits.items():
    print(fruit, color)


# Use enumerate() function to retrieve position index and value when looping through a sequence
fruits = ['orange', 'apple', 'pear']
for i, fruit in enumerate(fruits):
    print(i, fruit)


# Use zip() function to loop over two or more sequence at the same time
fruits = ['orange', 'apple', 'pear', 'banana']
colors = ['orange', 'red', 'yellow', 'yellow']
for fruit, color in zip(fruits, colors):
    print(fruit, color)


# Use reversed() function to loop over a sequence in reverse
fruits = ['orange', 'apple', 'pear', 'banana']
for fruit in reversed(fruits):
    print(fruit)


# Use sorted() function to loop over a sequence in sorted order
fruits = ['orange', 'apple', 'pear', 'banana']
for fruit in sorted(fruits):
    print(fruit)


# Use sorted() in combination with set()
fruits_set = set(fruits)
print(sorted(fruits_set))
