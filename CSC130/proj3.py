'''
Kyle Finter
proj3.py
'''
string=input("Enter a phrase to be translated to Morse code: ")
string=string.upper()
liststr=list(string)
lengthlist=len(liststr)
count=0
while count<=lengthlist:
    for letter in liststr:
        count+=1
        if letter==',':
            liststr.insert(count,'--..--')
            liststr.remove(',')
        if letter=='.':
            liststr.insert(count,'.-.-.-')
            liststr.remove('.')
        if letter=='?':
            liststr.insert(count,'..--..')
            liststr.remove('?')
        if letter=='0':
            liststr.insert(count,'-----')
            liststr.remove('0')
        if letter=='1':
            liststr.insert(count,'.----')
            liststr.remove('1')
        if letter=='2':
            liststr.insert(count,'..---')
            liststr.remove('2')
        if letter=='3':
            liststr.insert(count,'...--')
            liststr.remove('3')
        if letter=='4':
            liststr.insert(count,'....-')
            liststr.remove('4')
        if letter=='5':
            liststr.insert(count,'.....')
            liststr.remove('5')
        if letter=='6':
            liststr.insert(count,'-....')
            liststr.remove('6')
        if letter=='7':
            liststr.insert(count,'--...')
            liststr.remove('7')
        if letter=='8':
            liststr.insert(count,'---..')
            liststr.remove('8')
        if letter=='9':
            liststr.insert(count,'----.')
            liststr.remove('9')
        if letter=='A':
            liststr.insert(count,'.-')
            liststr.remove('A')
        if letter=='B':
            liststr.insert(count,'-...')
            liststr.remove('B')
        if letter=='C':
            liststr.insert(count,'-.-.')
            liststr.remove('C')
        if letter=='D':
            liststr.insert(count,'-..')
            liststr.remove('D')
        if letter=='E':
            liststr.insert(count,'.')
            liststr.remove('E')
        if letter=='F':
            liststr.insert(count,'..-.')
            liststr.remove('F')
        if letter=='G':
            liststr.insert(count,'--.')
            liststr.remove('G')
        if letter=='H':
            liststr.insert(count,'....')
            liststr.remove('H')
        if letter=='I':
            liststr.insert(count,'..')
            liststr.remove('I')
        if letter=='J':
            liststr.insert(count,'.---')
            liststr.remove('J')
        if letter=='K':
            liststr.insert(count,'-.-')
            liststr.remove('K')
        if letter=='L':
            liststr.insert(count,'.-..')
            liststr.remove('L')
        if letter=='M':
            liststr.insert(count,'--')
            liststr.remove('M')
        if letter=='N':
            liststr.insert(count,'-.')
            liststr.remove('N')
        if letter=='O':
            liststr.insert(count,'---')
            liststr.remove('O')
        if letter=='P':
            liststr.insert(count,'.--.')
            liststr.remove('P')
        if letter=='Q':
            liststr.insert(count,'--.-')
            liststr.remove('Q')
        if letter=='R':
            liststr.insert(count,'.-.')
            liststr.remove('R')
        if letter=='S':
            liststr.insert(count,'...')
            liststr.remove('S')
        if letter=='T':
            liststr.insert(count,'-')
            liststr.remove('T')
        if letter=='U':
            liststr.insert(count,'..-')
            liststr.remove('U')
        if letter=='V':
            liststr.insert(count,'...-')
            liststr.remove('V')
        if letter=='W':
            liststr.insert(count,'.--')
            liststr.remove('W')
        if letter=='X':
            liststr.insert(count,'-..-')
            liststr.remove('X')
        if letter=='Y':
            liststr.insert(count,'-.--')
            liststr.remove('Y')
        if letter=='Z':
            liststr.insert(count,'--..')
            liststr.remove('Z')
print(' '.join(liststr))
