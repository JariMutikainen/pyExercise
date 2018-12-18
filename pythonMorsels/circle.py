#  This week I want you to make a class that represents a circle.
# 
# The circle should have a radius, a diameter, and an area. It should also
# have a nice string representation.
# 
# For example:
# 
# >>> c = Circle(5)
# >>> c
# Circle(5)
# >>> c.radius
# 5
# >>> c.diameter
# 10
# >>> c.area
# 78.53981633974483
# 
# Additionally the radius should default to 1 if no radius is specified
# when you create your circle:
# 
# >>> c = Circle()
# >>> c.radius
# 1
# >>> c.diameter
# 2
# 
# There are three bonuses for this exercise.
# 
# For the first bonus, make sure when the radius of your class changes
# that the diameter and area both change as well: ✔️
# 
# >>> c = Circle(2)
# >>> c.radius = 1
# >>> c.diameter
# 2
# >>> c.area
# 3.141592653589793
# >>> c
# Circle(1)
# 
# For the second bonus, make sure you can set the diameter attribute in
# your Circle class and the radius will update and also that you cannot
# set the area (setting area should raise an AttributeError): 
# 
# >>> c = Circle(1)
# >>> c.diameter = 4
# >>> c.radius
# 2.0
# 
# 
# For the third bonus, make sure your radius cannot be set to a negative
# number: ✔️
#
# 
# >>> c = Circle(5)
# >>> c.radius = 3
# >>> c.radius = -2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "circle.py", line 27, in radius
#     raise ValueError("Radius cannot be negative")
# ValueError: Radius cannot be negative
# 
# 

from math import pi

class Circle:

    def __init__(self, radius=1):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._area = pi * self._radius * self._radius

    def __repr__(self):
        return f'Circle({self._radius})'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = r
            self._diameter = 2 * self._radius
            self._area = pi * self._radius * self._radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, d):
        if d < 0:
            raise ValueError("diameter cannot be negative")
        else:
            self._diameter = d
            self._radius = self._diameter / 2.0
            self._area = pi * self._radius * self._radius
            
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, a):
        raise AttributeError

## Testing
#c = Circle(5)
#print(c)
#print(c.radius)
#print(c.diameter)
#print(c.area)
#c = Circle()
#print(c.radius)
#print(c.diameter)
#c = Circle(2)
#c.radius = 1
#print(c.diameter)
#print(c.area)
#print(c)
#c = Circle()
#c.diameter = 4
#print(c.radius)
##c.area = 3.14
##c.radius = -7

