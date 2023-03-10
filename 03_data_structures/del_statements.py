# Del statements

# Initiate a list and delete the 2nd item.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[1] # same as fruits.pop(1)
print (fruits)

# Initiate a list and delete slice 2-4
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[2:4]
print(fruits)

# Initiate a list and delete all the items
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[:] # same as fruits.clear()
print(fruits)
