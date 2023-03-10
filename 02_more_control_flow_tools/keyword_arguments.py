# Keyword Arguments

# Create function with 1 mandatory and 3 optional argument
def foo(name, age=18, gender='Male', address='Cavite'):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Address: {address}")

# Call defining function
# 1. Suppy required argument
foo('Jayson')

# 2. Supply required and any optional argument
foo('Jayson', address='Batangas')


# Using *args and **kwargs
def foo1(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

foo1('Jayson', 'Committee', 'Team', key1='Education', key2='Membership', key3='Media')

# Derive above function using *args and **kwargs
def foo2(name, *args, **kwargs):
    print(f"Name: {name}")

    for a in args:
        print(f"Other: {a}")
    
    for kw in kwargs:
        print(f"{kw.capitalize()}: {kwargs[kw]}")

foo2('Jayson', 'Kind', age=18, gender='Male', address='Batangas')
