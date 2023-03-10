# List Comprehensions

# assume we want to create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# we can calculate the list of squares without any side effects
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# or 1 liner for loop
squares = [x**2 for x in range(10)]
print(squares)

# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

# or 1 liner for loop for logic above
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)


# Another examples:
# apply a function to all the elements, example is abs() function
values = [-4, -2, 0, 2, 4]
absolute_values = [abs(x) for x in values]
print(absolute_values)

# apply a method to all the elements, example is capitalize() method
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
capitalize_fruits = [x.capitalize() for x in fruits]
print(capitalize_fruits)
