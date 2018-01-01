'''
Kyle Finter
proj01.py
Finter179
'''
INCHBILL=0.0043
MILESMOON=238857
import math
debt=float(input("What is the United States national debt? "))
denom=int(input("What denomination of U.S. currency bills do you want to use? "))
if denom>0:
    bills=debt/denom
    height=INCHBILL*bills
    heightinmiles=height/63360
    tripstomoon=heightinmiles/MILESMOON
    print("The debt", debt, "has a height in miles of", denom,"'s,", round(heightinmiles,6))
    print("That is", round(tripstomoon,11), "times the average distance from the earth to the moon.")
elif denom==0:
    print("You can't divide by zero.")
else:
    print("You can't have a negative bill denomination.")
input("Press any key to continue...")
