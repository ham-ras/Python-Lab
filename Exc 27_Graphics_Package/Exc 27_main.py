import graphics.circle
from graphics import rectangle

import graphics.graphics_3d.sphere
from graphics.graphics_3d.cuboid import area as cuboid_area
from graphics.graphics_3d.cuboid import perimeter as cuboid_peri

r=int(input("Enter the radius to find area and perimeter of circle : "))
a=graphics.circle.area(r)
p=graphics.circle.perimeter(r)
print("Area : ",a)
print("Perimeter : ",p)

l=int(input("\nEnter the length of rectagle : "))
b=int(input("Enter the breadth of rectagle : "))
a=rectangle.area(l,b)
p=rectangle.perimeter(l,b)
print("Area : ",a)
print("Perimeter : ",p)

print("")

a=cuboid_area()
print("Area of cuboid : ",a)

print("")

p=cuboid_peri()
print("Perimeter of cuboid : ",p)

graphics.graphics_3d.sphere.area()
graphics.graphics_3d.sphere.perimeter()



