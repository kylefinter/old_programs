/*
Kyle Finter
finter179
4/22/16
HW#6 checksum digit for ISBN-13 numbers
*/

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int toDigit(char ch){
    return ch-'0';//ascii values are subtracted
}

int checksumDigit(string isbnNumber){
    int digit, mDigit, sumDigit, multiDigit, check;

    for (int i=0;i<12;i=i+2){
        digit=toDigit(isbnNumber[i]);
        sumDigit=digit+sumDigit;
        mDigit=toDigit(isbnNumber[i+1]);
        multiDigit=mDigit*3+multiDigit;
    }

    check=10-(sumDigit+multiDigit)%10;
    if (check==10)
        return 0;
    else
        return check;
}

int main(){
    string isbn;
    ifstream infile;
    infile.open("isbn.txt");
    if (!infile){
        cout << "Error opening file";
    }
    while (infile >> isbn){
        cout << checksumDigit(isbn) << endl;
    }
    infile.close();
    return 0;
}
