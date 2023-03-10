# Defining Functions

# Create an adder function with an items or list parameter
def adder(items):
    s = 0
    for n in items:
        s += n
    
    print(s)

# # Call the definition
items = [4, 6, 10]
adder(items)


# Create fibonacci function using while
# while - sets aside a block of code that is to be executed repeatedly until a condition is falsified
def fib(n):
    a = 0
    b = 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b

# Call the function
fib(2000)