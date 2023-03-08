# Del statements

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[1] # same as fruits.pop(1)
print (fruits)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[2:4]
print(fruits)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
del fruits[:] # same as fruits.clear()
print(fruits)
