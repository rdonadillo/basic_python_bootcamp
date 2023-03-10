# Exercise 1: Write a program that calculates the area of a circle given the radius (area=πr²)
radius = 4
area = 3.14 * radius * radius
print("radius:", radius)
print("area:", area)

# E1 Bonus: User can enter the radius value (hint: cast input to int type)
#           Make use of advanced math operators (squared)
radius = int(input("Enter radius:"))
area = 3.14 * radius ** 2
print("Circle area:", area)