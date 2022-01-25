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

rect1=Rectangle(3,4)
rect2=Rectangle(4,5)
rect1.area()
peri=rect1.perimeter()
print("Perimeter : ",peri)
print("")
rect2.area()
peri=rect2.perimeter()
print("Perimeter : ",peri)

if rect1.a == rect2.a:
    print("both are equal")
else:
    print("both are not equal")

    
