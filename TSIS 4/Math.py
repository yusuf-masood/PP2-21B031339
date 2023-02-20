
import math

def deg_to_rad(degrees):
    radians = degrees * math.pi / 180
    return radians

degrees = float(input(" input the degree: "))
radians = deg_to_rad(degrees)
print("{} degrees is equal to {} radians.".format(degrees, radians))





#Trapezoid
def calculate_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))

area = calculate_area(base1, base2, height)

print("The area of the trapezoid is:", area)






#Polygon

def calculate_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

n = int(input("Enter the number of sides of the polygon: "))
s = float(input("Enter the length of each side of the polygon: "))

area = calculate_area(n, s)

print("The area of the regular polygon is:", area)





#Parallelogram
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = base * height

print("The area of the parallelogram is:", area)

