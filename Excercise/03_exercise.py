# Exercise 3: Write a program that calculates the circle area for each radius in a list
radiuses = [1, 2, 3, 5, 8, 13]

def circle_area(radius):
    return 3.14 * radius ** 2

for radius in radiuses:
    print("radius:", radius, " area: ", circle_area(radius))

# E3 Bonus: User can input the radiuses (Hint: looping input)
radiuses = []
answer = 'y'
while answer == 'y':
    radius = int(input("Enter radius:"))
    radiuses.append(radius)
    answer = input("Add another [y/n]?:")

def circle_area(radius):
    return 3.14 * radius ** 2

for radius in radiuses:
    print("radius:", radius, " area: ", circle_area(radius))