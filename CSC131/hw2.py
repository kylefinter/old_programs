'''
Kyle Finter
Homework 2
Circle 2D'''
import math
class Circle2D():
    def __init__(self,x=0,y=0,radius=0):
        self.__x=x
        self.__y=y
        self.__radius=radius
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getRadius(self):
        return self.__radius
    def setRadius(self,radius):
        self.__radius=radius
    def __str__(self):
        return 'Circle with center ('+str(self.__x)+','+str(self.__y)+') and radius '+str(self.__radius)
    def getArea(self):
        return math.pi*(self.__radius**2)
    def getPerimeter(self):
        return 2*math.pi*self.__radius
    def containsPoint(self,x,y):
        distance=math.sqrt(((y-self.__y)**2)+((x-self.__x)**2))
        if distance<self.__radius:
            return True
        else:
            return False
    def contains(self,circle2D):
        if circle2D.__radius*2<=self.__radius:
            return True
        else:
            return False
    def overlaps(self,circle2D):
        if circle2D.__radius<self.__radius+circle2D.__radius:
            return True
        else:
            return False
    def __contains__(self,anotherCircle):
        if self.contains(anotherCircle):
            return True
        else:
            return False
    def __lt__(self,anotherCircle):
        return self.__radius<anotherCircle.__radius
    def __le__(self,anotherCircle):
        return self.__radius<=anotherCircle.__radius
    def __gt__(self,anotherCircle):
        return self.__radius>anotherCircle.__radius
    def __ge__(self,anotherCircle):
        return self.__radius>=anotherCircle.__radius
    def __eq__(self,anotherCircle):
        if type(self)==type(anotherCircle):
            return self.__radius==anotherCircle.__radius
        else:
            return False
    def __ne__(self,anotherCircle):
        if type(self)!=type(anotherCircle):
            return True
        else:
            return self.__radius!=anotherCircle.__radius
        
def main():
    x = 0#float(input("Enter x coordinate for the center of circle 1: "))
    y = 0#float(input("Enter y coordinate for the center of circle 1: "))
    r = 4#float(input("Enter the radius of circle 1: "))
    c1 = Circle2D(x, y, r)
    print(c1)
    
    x = 1#float(input("\nEnter x coordinate for the center of circle 2: "))
    y = 0#float(input("Enter y coordinate for the center of circle 2: "))
    r = 1#float(input("Enter the radius of circle 2: "))
    c2 = Circle2D(x, y, r)
    print(c2)

    #Test the getArea() and getPerimeter() methods
    print("\nArea of a %s is %0.2f" % (c1, c1.getArea()))
    print("Perimeter of a %s is %0.2f" % (c1, c1.getPerimeter()))

    print("\nArea of a %s is %0.2f" % (c2, c2.getArea()))
    print("Perimeter of a %s is %0.2f" % (c2, c2.getPerimeter()))
    #-------------------

    #Test containsPoint() method
    print("\nResult of c1.containsPoint(c2.getX( ), c2.getY( )) is",
          c1.containsPoint(c2.getX( ), c2.getY( )))

    #Test contains() method
    if c1.contains(c2):
        print("\n%s contains %s" % (c1, c2))
    else: 
        print("\n%s does not contain %s" % (c1, c2))
                                          
    print("\nResult of c2.contains(c1) is",
           c2.contains(c1))
    #----------------

    #Test overlap() method
    if c1.overlaps(c2):
        print("\n%s overlaps with %s" % (c1,c2))
    else: 
        print("\n%s does not overlap with %s" % (c1,c2))
    #--------------

    #Test overloaded in operator                                     
    print("\nResult of c2 in c1 is", c2 in c1)                     

    #Testing overloaded comparison and equality operators
    #Something similar to this
    print("\nTesting overloaded comparison operators...")
    print("c1 == c2?", c1 == c2)
    print("c1 != c2?", c1 != c2)
    print("c1 < c2?", c1 < c2)
    print("c1 <= c2?", c1 <= c2)
    print("c1 > c2?", c1 > c2)
    print("c1 >= c2?", c1 >= c2)
    print('c1 == "Hello"?', c1 == "Hello")
    print('c1 != "Hello"?', c1 != "Hello")
    
main()
