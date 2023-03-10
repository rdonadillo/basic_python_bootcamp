# Break and Continue

# Breaks out of innermost enclosing loop
# Print first item on a list that has 0 remainder
for n in range(2, 10):
    if n % 2 == 0:
        print(n)
        break
    
    print('END')

# Print eact item on a list that has 0 remainder
for n in range(2, 10):
    if n % 2 == 0:
        print(n)
        continue

    print('END')


# Pass

# Do nothing or no action
# Print each item on a list that has a remainder
for n in range(2, 10):
    if n % 2 == 0:
        pass
    else:
        print(n)
