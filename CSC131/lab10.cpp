/*
Author: Kyle Finter
Date: 4/12/2016
File name: lab10.cpp
Description: determines if date is equal to magic date
*/

#include <iostream>
#include <string>
using namespace std;

bool isMagicDate(int month, int day, int year){
    if ((month*day)==year)
        return true;
    else
        return false;
}

int main()
{
    string date, monthStr, firstStr, secondStr, thirdStr;
    int month, day, year, firstInt, secondInt, thirdInt;
    bool isMagic;
    cout << "Enter date in the format mm/dd/yy ";
    getline(cin,date,'\n');
    firstInt=date.find('/');
    monthStr=date.substr(0,firstInt);
    month=stoi(monthStr);

    secondInt=date.find('/',firstInt+1);
    secondStr=date.substr(firstInt+1,secondInt-1);
    day=stoi(secondStr);

    thirdInt=date.find('/',secondInt+1);
    thirdStr=date.substr(secondInt+1,thirdInt-1);
    year=stoi(thirdStr);

    cout << "month is " << month << '\n';
    cout << "day is " << day << '\n';
    cout << "year is " << year << '\n' << '\n';
    isMagic=isMagicDate(month, day, year);
    if (isMagic)
        cout << date << " is a magic date";
    else
        cout << date << " is not a magic date";
    return 0;
}

