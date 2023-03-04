# Range

# Iterate over a sequence of numbers using built-in function range()
for i in range(4):
    print(i)


print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
