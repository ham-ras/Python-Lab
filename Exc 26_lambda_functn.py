a=int(input("Enter the side of square : "))
l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
b1=int(input("Enter the base of triangle : "))
h=int(input("Enter the height of triangle : "))
s=lambda a : a*a
r=lambda l,b : l*b
t=lambda b1,h : (b1*h)/2
print("Area of square = ",s(a))
print("Area of rectangle = ",r(l,b))
print("Area of triangle = ",t(b1,h))
