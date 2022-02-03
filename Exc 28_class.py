class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        self.a=self.l*self.b
        print("Area : ",self.a)
    def perimeter(self):
        self.p=2*(self.l+self.b)
        return(self.p)
    def compare(self,rectangle):
        if self.a == rectangle.a:
            print("both are equal")
        else:
            print("both are not equal")


l1=int(input("Enter the length rectangle 1 : "))
b1=int(input("Enter the breadth rectangle 1 : "))
rect1=Rectangle(l1,b1)
rect1.area()
peri=rect1.perimeter()
print("Perimeter : ",peri)
print("")

l2=int(input("Enter the length rectangle 2 : "))
b2=int(input("Enter the breadth rectangle 2 : "))
rect2=Rectangle(l2,b2)
rect2.area()
peri=rect2.perimeter()
print("Perimeter : ",peri)

rect1.compare(rect2)


    
