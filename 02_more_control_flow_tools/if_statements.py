# If Statements

# Create an if statement given an integer and print if that is a Negative, Zero, Single or More
x = int(input("Please enter an integer: "))

if x < 0:
    print('negative')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')