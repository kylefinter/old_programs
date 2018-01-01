'''Kyle Finter
finter179
lab4
Inheritance'''
import math
class GeometricObject(object):
    def __init__(self, color = "white", filled = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled
  
    def __str__(self):
        return "color: " + self.color + \
            " and filled: " + str(self.filled)
class Circle(GeometricObject):
    '''Class Circle inherits from GeometricObject'''
    def __init__(self,radius=1.0,color='white',filled=True):
        GeometricObject.__init__(self,color,filled)
        self._radius=radius
    def getArea(self):
        return 3.1415*self._radius**2
    def getPerimeter(self):
        return 2*3.1415*self._radius
    def __str__(self):
        return 'Circle: radius='+str(self._radius)+' '+GeometricObject.__str__(self)
class Triangle(GeometricObject):
    '''Class Triangle inherits from GeometricObject'''
    def __init__(self,side1=1.0,side2=1.0,side3=1.0,color='white',filled=True):
        GeometricObject.__init__(self,color,filled)
        self._side1=side1
        self._side2=side2
        self._side3=side3
    def getArea(self):
        s=(self._side1+self._side2+self._side3)/2
        return round(math.sqrt(s*(s-self._side1)*(s-self._side2)*(s-self._side3)),2)
    def getPerimeter(self):
        return self._side1+self._side2+self._side3
    def __str__(self):
        return 'Triangle: side1='+str(self._side1)+' side2='+str(self._side2)+' side3='+str(self._side3)+' '+GeometricObject.__str__(self)
def main():
    #Testing Circle class
    c = Circle(5, "blue", False)
    print(c)
    print()
    
    print("Entering input values for a circle")
    r = float(input('Enter value for radius: '))

    c1 = Circle(r)
    
    print(c1)
    print("%.2f" % c1.getArea())
    print("%.2f" % c1.getPerimeter())
    print(c1.getColor())
    print(c1.isFilled())

    #Testing Triangle class
    print("\nEntering input values for a traingle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color = input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == "1")
    t1 = Triangle(s1, s2, s3, color, filled)

    print(t1)
    print("%.2f" % t1.getArea())
    print("%.2f" % t1.getPerimeter())
    print(t1.getColor())
    print(t1.isFilled())
main()
