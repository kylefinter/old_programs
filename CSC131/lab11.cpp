/*
Author: Kyle Finter
Date: 4/20/2016
File name: lab12.cpp
Description: find the standard deviation of an array of numbers
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

double standardDeviation(double arrayOfNumbers[], const int arraySize) {
	double deviate, N, summation=0.0, U=0.0;
	N = 1 / (double)arraySize;
	for (int i = 0; i<arraySize; i++) {
		U = arrayOfNumbers[i] + U;
	}
	U = U / (double)arraySize;

	for (int j = 0; j<arraySize; j++) {
		summation = pow((arrayOfNumbers[j] - U), 2.0) + summation;
	}

	return deviate = sqrt(N*summation);
}

double standardDeviation(vector<double> numVector) {
	double vDeviate, N, summation=0.0, U=0.0;
	N = 1 / (double)numVector.size();
	for (double val : numVector) {
		U = val + U;
	}
	U = U / (double)numVector.size();

	for (double val1 : numVector) {
		summation = pow((val1 - U), 2.0) + summation;
	}
	return vDeviate = sqrt(N*summation);
}

int main() {
	double dev, vDev;
	const int SIZE = 20;
	double myList[SIZE] = { 2,11,4,5,9,5,4,12,7,8,9,3,7,4,12,10,9,6,9,4 };
	dev = standardDeviation(myList, SIZE);
	cout << fixed <<setprecision(2)<<dev<<endl;
	vector<double> myVector(SIZE);
	for (int i = 0; i<SIZE; i++) {
		myVector[i] = myList[i];
	}
	vDev = standardDeviation(myVector);
	cout << vDev;
	return 0;
}
