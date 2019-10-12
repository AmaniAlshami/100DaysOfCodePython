class Shape :
     def __init__(self,length,width):
       self.length = length
       self.width = width
    
class Trapezoid(Shape):
    def __init__(self,length,width,base):
        super().__init__(length,width)
        self.base = base 
    def trapezoid_area(self):
      return ((self.width * self.base)*0.5)*self.length

     
class Triangle(Shape):
    def triangle_area(self):
          return (self.width * self.length)*0.5


shape1 = Triangle(length=3,width=4) 
print("Area of Triangle ",shape1.triangle_area())
shape2 =Trapezoid(length=2,width=7,base=3)
print("Area of Trapezoid ",shape2.trapezoid_area())
