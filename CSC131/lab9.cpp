/*
Author: Kyle Finter
Date: 4/5/2016
File name: lab1.cpp
Description: calculates retail price
*/

#include <iostream>
#include <string>
using namespace std;

float calculateRetail(float cost, float percent){
    return cost+(cost*(percent/100));
}

int main()
{
    string name;
    float cost, percent, price;
    cout << "Enter item description: ";
    getline(cin,name,'\n');
    cout << "You entered " << name << '\n';
    cout << "Enter item wholesale cost: ";
    cin >> cost;
    cout << "You entered " << cost << '\n';
    cout << "Enter item markup percentage: ";
    cin >> percent;
    cout << "You entered " << percent << '\n' << '\n';
    price=calculateRetail(cost, percent);
    cout << "Retail price for " << name << " is " << price;
    return 0;
}

