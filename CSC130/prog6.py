'''Kyle Finter
Project 6
Section 002'''
class BMI():
    def __init__(self,name='Bob',age=0,weight=0.0,height=0.0):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height

    def get_Status(self):
        BMI=self.get_BMI()
        if BMI<18.5:
            return 'Underweight'
        if BMI>=18.5 and BMI<25:
            return 'Normal'
        if BMI>=25 and BMI<30:
            return 'Overweight'
        if BMI>30:
            return 'Obese'
    def get_Name(self):
        return self.__name
    def get_Age(self):
        return self.__age
    def get_Weight(self):
        return self.__weight
    def get_Height(self):
        return self.__height
    def get_BMI(self):
        height=self.__height/39.3700787
        weight=self.__weight/2.20462262
        BMI=weight/height**2
        return round(BMI,2)

import sys
def test(did_pass):
    """Print the result of a test"""
    linenum=sys._getframe(1).f_lineno
    if did_pass:
        msg="Test at line {0} ok.".format(linenum)
    else:
        msg="Test at line {0} failed.".format(linenum)
    print(msg)
def main():
    bmi1=BMI("John Doe",18,145,70)
    print("The BMI for",bmi1.get_Name(), "is",bmi1.get_BMI(),bmi1.get_Status())
    bmi2=BMI("Sue Doe",19,103,68)
    print("The BMI for",bmi2.get_Name(), "is",bmi2.get_BMI(),bmi2.get_Status())
    bmi3=BMI("Pete Doe",50,217,70)
    print("The BMI for",bmi3.get_Name(), "is",bmi3.get_BMI(),bmi3.get_Status())
main()
input("Press any key to continue...")
