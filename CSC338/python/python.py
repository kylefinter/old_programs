import sys
import string

def readfile(textFile):
	f = open(textFile,'r')
	fileStr = f.read()
	returnStr = ''
	for x in fileStr:
		if x not in string.punctuation:
			returnStr = returnStr + x
	return returnStr

def countchars(oldString):
	myDictionary = {}
	for x in oldString:
		if x not in myDictionary:
			myDictionary[x] = 1
		else:
			myDictionary[x] += 1
	return myDictionary
	
def countwords(listOfWords):
	myDictionary = {}
	for x in listOfWords:
		if x not in myDictionary:
			myDictionary[x] = 1
		else:
			myDictionary[x] += 1
	return myDictionary
	
def showcounts(printDictionary):
	for key, values in sorted(printDictionary.items()):
		print(key,':',values)
	return

def main():
	textFile = sys.argv[1]

	removePunctuation = readfile(textFile)
	print(removePunctuation)
	
	characterCount = countchars('Rollercoaster')
	showcounts(characterCount)
	
	wordList = ['hi','hi','bye','later']
	wordCount = countwords(wordList)
	showcounts(wordCount)

	return
	
main()