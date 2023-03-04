# Defining Functions

# Create definition
def adder(items):
    s = 0
    for n in items:
        s += n
    
    print(s)

# # Call the definition
items = [4, 6, 10]
adder(items)


# Create fibonacci function
def fib(n):
    a = 0
    b = 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b

# Call the function
fib(2000)