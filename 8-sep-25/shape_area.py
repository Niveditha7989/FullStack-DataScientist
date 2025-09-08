'''4. Shape Area Calculator
 
Base Class (Shape):
 
*Attribute: name
*Method: area() → to be overridden by subclasses
 
Subclasses:
 
* Circle(radius) → area = π × r²
* Rectangle(width, height) → area = width × height
 
Example:
 
python
c = Circle(7)
print(c.area())
r = Rectangle(4, 5)
print(r.area())

 
Output:
 

153.94
20'''

import math
class Shape:
    def __init__(self, name="Shape"):
        self.name = name
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
c = Circle(7)
print(c.area())    

r = Rectangle(4, 5)
print(r.area())    
