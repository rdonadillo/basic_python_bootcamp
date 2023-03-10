# Append
# Create a list and add an item to the end of the list. Equivalent to a[len(a):] = [x].
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('grapes')
print(fruits)

# Extend
# Create a list and extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable
old_fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits = ['mango', 'grapes']
fruits.extend(old_fruits)
print(fruits)

# Insert
# Create a list and insert an item at a given position.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.insert(3, 'grapes')
print(fruits)

# Remove
# Create a list and remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.remove('banana')
print(fruits)

# Pop
# Create a list and remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.pop(3)
print(fruits)

# Clear
# Create a list and remove all items from the list. Equivalent to del a[:].
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.clear()
print(fruits)

# Index
# Create a list and return zero-based index in the list of the item whose value is equal to x. Raises a ValueError if there is no such item.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
index = fruits.index('pear')
print(index)

# Count
# Create a list and return the number of times x appears in the list.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
count = fruits.count('banana')
print(count)

# Sort
# Create a list and sort the items of the list in place.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# Reverse
# Create a list and reverse the elements of the list in place.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
print(fruits)

# Copy
# Create a list and return a shallow copy of the list. Equavalent to a[:].
old_fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
new_fruits = old_fruits.copy()
print(new_fruits)
# Below is using '=', but new list is always equal old list even new list updated
old_fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
new_fruits = old_fruits
new_fruits.append('grapes')
print(new_fruits)
print(old_fruits)
