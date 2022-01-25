def area() :
    l=int(input("Enter the length of the cuboid : "))
    b=int(input("Enter the breadth of the cuboid : "))
    h=int(input("Enter the height of the cuboid : "))
    a=2*((l*b)+(l*h)+(b*h))
    return(a)

def perimeter() :
    l=int(input("Enter the length of the cuboid : "))
    b=int(input("Enter the breadth of the cuboid : "))
    h=int(input("Enter the height of the cuboid : "))
    p=4*(l+b+h)
    return(p)