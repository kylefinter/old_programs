'''
Kyle Finter
Project 4
'''
def wordCount(filename):
    Commonwords={}
    file=open(filename,'r')
    for line in file:
        line=line.strip()
        wordlist=line.split(' ')
        for word in wordlist:
            word=word.lower()
            word=word.strip(' ,.?:;!-')
            if word in Commonwords:
                Commonwords[word]=Commonwords.get(word)+1
            else:
                Commonwords[word]=1
    file.close()
    prettyDictionary(Commonwords)

def prettyDictionary(dictionary):
    unique=len(dictionary)
    printlist=[]
    for key in dictionary:
        if dictionary[key]>3:
            printlist.append([key,dictionary[key]])
    printlist.sort()
    print('Length of dictionary:', unique)
    print('%-10s%5s' % ('Word','Count'))
    print('--------------------')
    for pair in printlist:
        print('%-10s%5i' % (pair[0],pair[1]))
    print('')

def compareFiles(firstfile,secondfile):
    intersection=0
    union=0
    symmdiff=0
    diff_first_second=0
    diff_second_first=0
    file1=open(firstfile,'r')
    firstset=set()
    for line in file1:
        line=line.strip()
        wordlist=line.split(' ')
        for word in wordlist:
            if len(word)>3:
                word=word.lower()
                word=word.strip(' ,.?:;!-')
                firstset.add(word)
    file1.close()
    file2=open(secondfile,'r')
    secondset=set()
    for line in file2:
        line=line.strip()
        wordlist=line.split(' ')
        for word in wordlist:
            if len(word)>3:
                word=word.lower()
                word=word.strip(' ,.?:;!-')
                secondset.add(word)
    file2.close()
    interset=firstset.intersection(secondset)
    intersection=len(interset)
    unionset=firstset.union(secondset)
    union=len(unionset)
    symmdiffset=firstset.symmetric_difference(secondset)
    symmdiff=len(symmdiffset)
    firstsetdiff=firstset.difference(secondset)
    diff_first_second=len(firstsetdiff)
    secondsetdiff=secondset.difference(firstset)
    diff_second_first=len(secondsetdiff)
    print('%-21s%-6s' % ('Operation','Result'))
    print('--------------------------')
    print('%-21s%-6i' % ('Union',union))
    print('%-21s%-6i' % ('Intersection',intersection))
    print('%-21s%-6i' % ('Symmetric Difference',symmdiff))
    print('%-21s%-6i' % ('Ga-DoI',diff_first_second))
    print('%-21s%-6i' % ('DoI-Ga',diff_second_first))
    print('')
    prettySet(interset)

def prettySet(prettyset):
    listofwords=[]
    for word in prettyset:
        listofwords.append(word)
    listofwords.sort()
    for word in listofwords:
        print('%-15s' % word)

def main():
    wordCount('gettysBurg.txt')
    wordCount('declarationOfInd.txt')
    compareFiles('gettysBurg.txt','declarationOfInd.txt')
main()
