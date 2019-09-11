from shape2 import *                                                       #importing everything from shape2 file

#class of 3-dimentional shape Box              
class Box(Rectangle):                                                      #class box inherits from class Rectangle 
      def __init__(self, length, width, height):                           #constructor method with length,width and height as attributes
          super().__init__(length,width)                                   #inherits constructor method from super class Rectangle
          self.height = height                                             #attribute height
      def __iadd__(self,other):                                            #method for overloading append operator
          super().__iadd__(other)                                          #inherits method from super class Rectangle
          self.height += other.height
          return self
      def area(self):                                                      #method for area of Box
          area = Rectangle.area(self)                                      #inherits Rectangle area
          peri = Rectangle.perimeter(self)                                 #inherits Rectangle perimeter
          return ((2*area) + (self.height*peri))                           #return area of box
      def volume(self):                                                    #method for volume of Box
          area = Rectangle.area(self)                                      #inherits Rectangle area
          return (self.height*area)                                        #return volume of box
      def __str__(self):                                                   #method to print attributes of Box
          return 'length = %.2f : width = %.2f : height = %.2f' %(self.length,self.width,self.height)

#class of 3-dimentional shape Cube
class Cube(Square):                                                        #class Cube inherits from class Square
      def __init__(self, side):                    
          super().__init__(side)                                           #inherits constructor method from super class Square
      def area(self):                                                      #method for area of Cube
          area = Square.area(self)                                         #inherits Square area
          return 6*area                                                    #return area of cube
      def volume(self):                                                    #method for volume of Cube
          area = Square.area(self)                                         #inherits Square area
          return(self.length*area)                                         #return volume of cube
      def __str__(self):                                                   #method to print attributes of Cube
          return 'length = %.2f '  %(self.length)

#class of 3-dimentional shape Cylinder
class Cylinder(Circle):                                                    #class Cylinder inherits from class Circle
      def __init__(self, radius, height):         
          super().__init__(radius)                                         #inherits constructor method from super class Circle
          self.height = height                                             #attribute height
      def __iadd__(self,other):                                            #method for overloading append operator
          super().__iadd__(other)                                          #inherits method from super class Circle
          self.height += other.height
          return self
      def area(self):                                                      #method for area of Cylinder
          area = Circle.area(self)                                         #inherits Circle area
          peri = Circle.perimeter(self)                                    #inherits Circle perimeter
          area1 = self.height*peri
          return ((2*area) + area1)                                        #returns area of cylinder
      def volume(self):                                                    #method for volume of Cylinder
          area = Circle.area(self)                                         #inherits Circle area
          return (self.height*area)                                        #returns volume of cylinder
      def __str__(self):                                                   #method to print the attributes of Cylinder
          return 'radius = %.2f : height = %.2f ' %(self.radius,self.height)

#class of 3-dimentional shape Cone
class Cone(Circle):                                                        #class Cone inherits from class Circle
      def __init__(self, radius, height):
          super().__init__(radius)                                         #inherits constructor method from super class Circle
          self.height = height                                             #attribute height
      def __iadd__(self,other):                                            #method for overloading append operator
          super().__iadd__(other)                                          #inherits method from super class Circle
          self.height += other.height
          return self
      def area(self):                                                      #method for area of Cone
          area = Circle.area(self)                                         #inherits Circle area
          s = (self.radius*self.radius + self.height*self.height) ** (1/2)
          peri = Circle.perimeter(self)                                    #inherits Circle perimeter
          area1 = (s*peri)/2
          return (area + area1)                                            #returns area of Cone
      def volume(self):                                                    #method for volume of Cone
          area = Circle.area(self)                                         #inherits Circle area
          return (self.height*area)/3                                      #returns volume of Cone
      def __str__(self):                                                   #method to print the attributes of Cone
          return 'radius = %.2f : height = %.2f ' %(self.radius,self.height)

#class of 3-dimentional shape Sphere
class Sphere(Circle):                                                      #class Sphere inherits from class Circle
      def __init__(self, radius):                 
          super().__init__(radius)                                         #inherits constructor method from super class Circle
      def area(self):                                                      #method for area of Sphere
          area = Circle.area(self)                                         #inherits Circle area
          return 4*area                                                    #returns area of sphere
      def volume(self):                                                    #method for volume of Sphere
          area = Circle.area(self)                                         #inherits Circle area
          return (4*self.radius*area)/3                                    #returns volume of sphere
      def __str__(self):                                                   #method to print attributes of sphere
          return 'radius = %.2f  ' %(self.radius)

#class of 3-dimentional shape Tetrahedron
class Tetrahedron(equTriangle):                                            #class Tetrahedron inherits from class equTriangle
      def __init__(self , a = 0.00):
          super().__init__(a)                                              #inherits constructor method from super class equTriangle
      def area(self):                                                      #method for area of Tetrahedron
          area = equTriangle.area(self)                                    #inherits area of equTriangle
          return 4*area                                                    #returns area of tetrahedron
      def volume(self):                                                    #method for volume of Tetrahedron
          area = equTriangle.area(self)                                    #inherits area of equTriangle
          h = (2 ** (1/2))*self.a/3 ** (1/2)                               #computing height of Tetrahedron
          return (h*area)/3                                                #returns volume of tetrahedron
      def __str__(self):                                                   #method to print attributes of Tetrahedron
          return 'length = %.2f ' %(self.a)

      