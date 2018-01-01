'''
Kyle Finter
proj03.py
Takes a string and transcodes them into morse code using a space as a delimiter between letters.
'''
string=input("Enter a phrase to be translated to Morse code: ")
string=string.upper()
liststr=list(string)
#(.=0)(,=27)(?=28)(0-9=29-38)
letterlist=['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','?','0','1','2','3','4','5','6','7','8','9']
morselist=['.-.-.-','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','--..--','..--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
lengthlist=len(liststr)
count=0
while count<lengthlist:
    lettercount=0
    for char in letterlist:
        if liststr[count]==char:
            liststr.insert(count,morselist[lettercount])
            liststr.pop(count+1)
            break
        lettercount+=1
    count+=1
print(' '.join(liststr))
input("Press Enter to Continue...")
