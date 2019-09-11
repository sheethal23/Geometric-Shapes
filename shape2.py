

from shape import Shape                                #from shape file importing class Shape  

#class of 2-dimentional shape Rectangle 
class Rectangle(Shape):                                #Rectangle class inheriting class Shape 
      def __init__(self,length = 0.00 ,width = 0.00):  #constructor with attributes length and width
          self.length = length
          self.width = width
      def __iadd__(self,other):                        #method for overloading append operator
          self.length += other.length
          self.width += other.width
          return self
      def perimeter(self):                             #method for perimeter of rectangle
          return 2*(self.length+self.width)            #returns perimeter of rectangle
      def area(self):                                  #method for area of rectangle
          return self.length*self.width                #returns area of rectangle
      def __str__(self):                               #method to print attributes
          return 'length = %.2f : width = %.2f ' %(self.length,self.width)

#class of 2-dimentional shape Circle
class Circle(Shape):                                   #Circle class inheriting class Shape
      def __init__(self,radius):                       #constructor method with attribute radius
          self.radius = radius
      def __iadd__(self,other):                        #method for overloading append operator
          self.radius += other.radius
          return self
      def perimeter(self):                             #method for perimeter of circle
          return 2*3.14159*(self.radius)               #returns perimeter of circle
      def area(self):                                  #method for area of circle
          return 3.14159*self.radius*self.radius       #returns area of circle
      def __str__(self):                               #method to print attributes
          return 'radius = %.2f ' %(self.radius)

#class of 2-dimentional shape Triangle
class Triangle(Shape):                                 #Triangle class inheriting class Shape
      def __init__(self,a,b,c):                        #constructor method with attributes a,b,c
          self.a = a
          self.b = b
          self.c = c
      def __iadd__(self,other):                        #method for overloading append operator
          self.a += other.a
          self.b += other.b
          self.c += other.c
          return self
      def perimeter(self):                             #method for perimeter of traingle
          return self.a+self.b+self.c                  #returns perimeter of triangle
      def area(self):                                  #method for area of triangle
          peri = Triangle.perimeter(self)
          k = peri / 2
          A = k*(k-self.a)*(k-self.b)*(k-self.c)
          return A**(1/2)                              #returns area of triangle
      def __str__(self):                               #method for printing attributes
          return 'a = %.2f : b = %.2f : c = %.2f ' %(self.a,self.b,self.c)

#class of 2-dimentional shape Square
class Square(Rectangle):                               #class Square inheriting class Rectangle
      def __init__(self, side):
          super().__init__(side,side)                  #inherits the constructor method of super class Rectangle
      def __str__(self):                               #method to print the attributes.
          return 'length = %.2f ' %(self.length)

#class of 2-dimentional shape rightTriangle
class rightTriangle(Triangle):                         #class rightTriangle inherits class Triangle
      def __init__(self, a, b):
          super().__init__(a,b,(a*a+b*b)**(1/2))       #inherits the constructor method of super class Triangle
      def __str__(self):                               #method to print the attributes.
          return 'length = %.2f : height = %.2f ' %(self.a,self.b)

#class of 2-dimentional shape equTriangle
class equTriangle(Triangle):                           #class equTriangle inherits class Triangle
      def __init__(self, a):
          super().__init__(a,a,a)                      #inherits the constructor method of super class Triangle
      def __str__(self):                               #method to print the attributes.
          return 'length = %.2f ' %(self.a)




