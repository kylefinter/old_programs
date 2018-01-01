/*
Kyle Finter
finter179
4/22/16
lab12 asks user for dynamic array that can calculate average and output it
*/

#include <iostream>
#include <iomanip>

using namespace std;

void addThree(int *ptr){
    *ptr=*ptr+3;
}

int main(){
    double* numPtr=nullptr;
    int numDoubles;
    double sumNum;
    cout << "Enter an integer to store x amount of doubles: ";
    cin >> numDoubles;
    numPtr=new double[numDoubles];
    for (int i=0;i<numDoubles;i++){
        double n=0;
        cout << "Enter a number to be stored in array: ";
        cin >> n;
        numPtr[i]=n;
        sumNum=n+sumNum;
    }
    delete [] numPtr;
    numPtr=nullptr;
    cout << "Average is " << sumNum/numDoubles << endl;

    int digit=0;
    int *digitPtr=nullptr;
    digitPtr=&digit;
    addThree(digitPtr);
    cout << digit << " was incremented by 3";
    return 0;
}
