# Exercise 2: Write a program that displays the circle area of radiuses from 1 to 100
for radius in range(1, 101):
    area = 3.14 * radius ** 2
    print("radius:", radius, " area: ", area)

# E2 Bonus: Wrap the circle area calculator inside a function accepting radius as parameter
def circle_area(radius):
    return 3.14 * radius ** 2

for radius in range(1, 101):
    print("radius:", radius, " area: ", circle_area(radius))