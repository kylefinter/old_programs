'''
Kyle Finter
Finter179
proj02
'''
code=""
while code!="z":
    code=input("Enter customer code: ")
    if code=="z":
        break
    begmeter=int(input("Enter beginning meter reading: "))
    endmeter=int(input("Enter ending meter reading: "))
    galwater=endmeter-begmeter
    if galwater<0:
        endmeter=endmeter+1000000000
        galwater=endmeter-begmeter
        endmeter=endmeter-1000000000
    if code=="r":
        bill=5.00+(0.0005*galwater)
    elif code=="c":
        if galwater<=4000000:
            bill=1000
        else:
            bill=1000+((galwater-4000000)*0.00025)
    elif code=="i":
        if galwater<=4000000:
            bill=1000
        elif galwater>4000000 and galwater<=10000000:
            bill=2000
        elif galwater>10000000:
            bill=2000+((galwater-10000000)*0.00025)
    print("Customer code:",code)

    print("Beginning meter reading:",begmeter)
    print("Ending meter reading:",(endmeter))

    print("Gallons of water used: %0.1f"%float(galwater/10))
    print("Amount billed: $%0.2f"%bill)
