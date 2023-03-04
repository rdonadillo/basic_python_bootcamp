# Break and Continue

# Breaks out of innermost enclosing loop
for n in range(2, 10):
    if n % 2 == 0:
        print(n)
        break
    
    print('END')


for n in range(2, 10):
    if n % 2 == 0:
        print(n)
        continue

    print('END')


# Pass

# Do nothing or no action
for n in range(2, 10):
    if n % 2 == 0:
        pass
    else:
        print(n)
