class square:
    a=float(input("enter a number: "))

    def area(self):
        area=self.a*self.a
        print(area)

    def perimeter(self):
        perimeter=4*self.a
        print(perimeter)

c=square()
x=c.area()
x=c.perimeter()
