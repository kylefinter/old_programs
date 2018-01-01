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

int toDigit(char ch) {
	return ch - '0';//ascii values are subtracted
}

int checksumDigit(string isbnNumber) {
	int digit, sumDigit, multiDigit, check;

	for (int i = 0; i<12; i = i + 2) {
		digit = toDigit(isbnNumber[i]);
		sumDigit = digit + sumDigit;
	}
	for (int j = 1; j<12; j = j + 2) {
		digit = toDigit(isbnNumber[j]);
		multiDigit = digit * 3 + multiDigit;
	}
	check = 10 - (sumDigit + multiDigit) % 10;
	return check;
}

int main() {
	string checksum, isbn;
	ifstream infile;
	infile.open("isbn.txt");
	if (!infile) {
		cout << "Error opening file";
	}
	while (infile >> isbn) {
		string checknumber;
		checksum = checksumDigit(isbn);
		checknumber = to_string(checksum);
		cout << checknumber << endl;
	}
	infile.close();
	return 0;
}
