# Sets

# Create simple set of fruits
fruits = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
print(fruits)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

# Print letters in 'a' but not in 'b'
print(a - b)

# Print letters in 'a' or 'b' or both
print(a | b)

# Print letters in both 'a' and 'b'
print(a & b)

# Print letters in 'a' or 'b' but not both
print(a ^ b)
