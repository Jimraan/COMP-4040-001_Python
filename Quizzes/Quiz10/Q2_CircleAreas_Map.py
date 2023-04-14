# Quiz 10  Question 2
# The formula of an area of a circle is known as A = π * r2 where r is the radius.
# The following list represents the radius values of five circles.
# radius_list = [3.5, 9.4, 7.1, 2.8, 5.0]
# Using Python, display a new list of areas of those circles.
radius_list = [3.5, 9.4, 7.1, 2.8, 5.0]


def area(radius):
    return 3.14 * radius**2

print("Radii: ", radius_list)
res = list(map(area, radius_list))
print("No Lambda: ", res)
res = list(map(lambda x: 3.14*x**2, radius_list))
print("With Lambda: ", res)
