# Range

# Iterate over a sequence of numbers using built-in function range()
# Iterate range(4) using for loop
for i in range(4):
    print(i)


# Create a list using range
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))


# Print each item of a list and identify its index
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
