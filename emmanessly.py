# CS 16X Git Assignment
print("Oceana and Emma's github assignment - CS 162")

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

# 1. rect_area (length, width) which will return the area of a rectangle - Emma's code
#creating a function that will return the computation for the area
def rect_area(length, width):
    area = length * width
    return area

#calling the function with the values inputed by the user
area = rect_area(length, width)
print("The area of your object is:", area)
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

def rect_solid_area(x, y, z):
    return 1
length = 1; width = 1; height = 1
rect_solid_area (length, width, height)

surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
