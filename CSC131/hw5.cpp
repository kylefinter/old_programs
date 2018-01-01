/*
Author: Kyle Finter
Date: 4/15/2016
File name: hw5.cpp
Description: convert from AM/PM to military time
*/

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

string convertToMilitaryTime(string regularTime){
    string hourStr, minuteStr, AMPM, finalTime;
    int hourPos, minutePos, AMPMPos, hour, minute, hours;

    hourPos=regularTime.find(':');
    hourStr=regularTime.substr(0,hourPos);
    hour=stoi(hourStr);
    if (hour!=12)
        hours=hour*100;

    minutePos=regularTime.find(' ', hourPos+1);
    minuteStr=regularTime.substr(hourPos+1,minutePos);
    minute=stoi(minuteStr);
    hours=hours+minute;

    AMPMPos=regularTime.find('\n',minutePos+1);
    AMPM=regularTime.substr(minutePos+1);

    if (AMPM[0]=='p' || AMPM[0]=='P')
        hours+=1200;
    finalTime=to_string(hours);
    switch (finalTime.length()){
    case 3:
        finalTime="0"+finalTime;
        break;
    case 2:
        finalTime="00"+finalTime;
        break;
    case 1:
        finalTime="000"+finalTime;
        break;
    }
    return finalTime;
}

int main(){
    string normalTime, milTime;

    cout << "Enter time: ";
    getline(cin,normalTime,'\n');

    milTime=convertToMilitaryTime(normalTime);
    cout << '\n' << "Corresponding military time is " << milTime << " hours";
}
