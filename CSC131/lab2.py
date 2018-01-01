'''Kyle Finter
finter179
Lab 2 Higher order functions'''
import functools
a=list(range(1,11))
print(a)
m=list(map(lambda x: x**3, a))
print(m)
f1=list(filter(lambda x: x%3==0, a))
print(f1)
r1=str(functools.reduce(lambda x,y: str(x)+str(y), a))
print(r1)
mL=[x**3 for x in a]
print(mL)
f1L=[x for x in a if x%3==0]
print(f1L)
aL=[x**3 for x in a if x%3==0]
print(aL)
def evenFilter(dictionary):
    return [dictionary.get(x) for x in dictionary if x%2==0]
data={1: 'one', 3: 'three', 4: 'four', 5: 'five', 8: 'eight', 10: 'ten'}
print(evenFilter(data))
def findMin(x,y):
    return [x if x<y else y]
print(findMin(1,9))
