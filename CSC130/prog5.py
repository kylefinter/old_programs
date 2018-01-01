'''Kyle Finter
Project 5
Section 002'''
def sumDigits(n):
    Sum=0
    for number in str(n):
        Sum=Sum+int(number)
    return Sum

def isValid(side1,side2,side3):
    if side1+side2>side3:
        return True
    else:
        return False

def convertMillis(millis):
    seconds=int(millis/1000)
    minutes=int(seconds/60)
    seconds=int(seconds%60)
    hours=int(minutes/60)
    minutes=minutes%60
    finalstr='%i:%i:%i' % (hours,minutes,seconds)
    return finalstr

def myPi(i):
    answer=0
    for x in range(1,i+1):
        numerator=(-1)**(x+1)
        denominator=((2*x)-1)
        answer=answer+(numerator/denominator)
    answer=round(4*answer,4)
    return answer

def BMI(w,h):
    height=h/39.3700787
    weight=w/2.20462262
    BMI=weight/height**2
    if BMI<18.5:
        return 'Underweight'
    if BMI>=18.5 and BMI<25:
        return 'Normal'
    if BMI>=25 and BMI<30:
        return 'Overweight'
    if BMI>30:
        return 'Obese'
import sys
def test(did_pass):
    """Print the result of a test"""
    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok.".format(linenum)
    else:
        msg="Test at line {0} failed.".format(linenum)
    print(msg)

def test_suite():
    test(sumDigits(142)==7)
    test(isValid(1,3,1)==True)
    test(convertMillis(555550000)=='154:19:10')
    test(myPi(101)==3.1515)
    test(BMI(146,70)=='Normal')
test_suite()
input("Press any key to continue...")
