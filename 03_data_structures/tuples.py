# Tuples

# It consists of a number of values separated by commas.
tups = 1, 2, 3
print(tups)
print(tups[0])

# Tuples may be nested
new_tups = tups, (4, 5, 6)
print(new_tups)

# Tuples are immutable
tups[0] = 88888 # TypeError: 'tuple' object does not support item assignment

# Tuples can contain mutable objects
mutable_tups = ([1, 2, 3], [4, 5, 6])
print(mutable_tups)