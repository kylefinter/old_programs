'''
Kyle Finter
Lab 3
Point class on Cartesian plane'''
import math
class Point():
    COUNT=0
    def __init__(self,x=0,y=0):
        self._x=x
        self._y=y
        Point.COUNT+=1
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def __str__(self):
        return '('+str(self._x)+', '+str(self._y)+')'
    def distance(self,point):
        dist=math.sqrt(((self._x-point.getX())**2)+((self._y-point.getY())**2))
        return dist
    def __distanceFromOrigin(self):
        dist=math.sqrt((self._x**2)+(self._y**2))
        return dist
    def __lt__(self,point):
        return Point._distanceFromOrigin(self)<Point._distanceFromOrigin(point)
    def __le__(self,point):
        return Point._distanceFromOrigin(self)<=Point._distanceFromOrigin(point)
    def __gt__(self,point):
        return Point._distanceFromOrigin(self)>Point._distanceFromOrigin(point)
    def __ge__(self,point):
        return Point._distanceFromOrigin(self)>=Point._distanceFromOrigin(point)
    def __eq__(self,point):
        if type(self)==type(point):
            return Point._distanceFromOrigin(self)==Point._distanceFromOrigin(point)
        else:
            return False
    def __ne__(self,point):
        if type(self)!=type(point):
            return True
        else:
            return Point._distanceFromOrigin(self)!=Point._distanceFromOrigin(point)
def main():
    p0=Point()
    print(p0)
    p1=Point(3,4)
    print(p1)
    p2=Point(3)
    print(str(Point.getX(p2))+' '+str(Point.getY(p2)))
    print(Point.distance(p1,p2))
    print('The distance between '+str(p1)+' and '+str(p2)+' is '+str(Point.distance(p1,p2)))
    print('Testing the comparison operators in the order <, <=, >, >=, ==, and !=')
    print('p1 < p2? '+str(p1<p2))
    print('p1 <= p2? '+str(p1<=p2))
    print('p1 > p2? '+str(p1>p2))
    print('p1 >= p2? '+str(p1>=p2))
    print('p1 == p2? '+str(p1==p2))
    print('p1 != p2? '+str(p1!=p2))
    print('')
    print('p1 == \"Hello\"? '+str(p1 is 'Hello'))
    print('p1 != \"Hello\"? '+str(p1 is not 'Hello'))
    print('')
    print('Number of point objects created is '+str(Point.COUNT))
main()
