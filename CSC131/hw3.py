'''
Kyle Finter
finter179
02/21/2016
HW3 Design a game using multiple classes'''

import random

class Card():
    def __init__(self,value,faceup):
        self.value=str(value)
        self.faceup=faceup

    def getValue(self):
        if self.faceup==True:
            return self.value
        else:
            return '*'

    def isFaceUp(self):
        return self.faceup

    def turn(self):
        self.faceup=not self.faceup
        return self.value

    def __str__(self):
        return str(self.getValue())

class Deck():
    def __init__(self,numCards):
        self.cards=[]
        for number in range(numCards):
            for num in range(2):
                c=Card(number+1,False)
                self.cards.append(c)
        
    def deal(self):
        if len(self)==0:
            return None
        else:
            return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)
        
    def __len__(self):
        return len(self.cards)    
    
class Game():
    Dlist=[]
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.numCards=((self.rows*self.columns)//2)
        
    def populateBoard(self):
        d=Deck(self.numCards)
        d.shuffle()
        for row in range(self.rows):
            rowList=[]
            for column in range(self.columns):
                rowList.append(d.deal())
            self.Dlist.append(rowList)
                
    def displayBoard(self):
        rowCounter=0
        rowString=''
        for row in self.Dlist:
            columnCounter=0
            for column in row:
                rowString=rowString+self.Dlist[rowCounter][columnCounter].getValue()+' '
                columnCounter+=1
            rowString=rowString+'\n'
            rowCounter+=1
        print(rowString)

    def turnCard(self,oneCoord,twoCoord):
        firstCoord=oneCoord
        secondCoord=twoCoord

        first=self.Dlist[int(oneCoord[0])-1][int(oneCoord[2])-1].turn()
        second=self.Dlist[int(twoCoord[0])-1][int(twoCoord[2])-1].turn()

        if first!=second:
            self.Dlist[int(oneCoord[0])-1][int(oneCoord[2])-1].turn()
            self.Dlist[int(twoCoord[0])-1][int(twoCoord[2])-1].turn()
            print('Not an identical pair. Found '+str(first)+' at '+firstCoord+\
                  ' and '+str(second)+' at '+secondCoord)
        
    def checkCoords(self,Coord):
        if int(Coord[0]) <=self.rows and int(Coord[2]) <= self.columns:
            return True
        else:
            return False

    def play(self):
        self.populateBoard()
        self.displayBoard()
        
        while True:
            oneCoord=input('Enter coordinates for first card ')
            if self.checkCoords(oneCoord)==True:
                twoCoord=input('Enter coordinates for second card ')
                if self.checkCoords(twoCoord)==False:
                    print('***Invalid coordinates! Try again.***')
            else:
                print('***Invalid coordinates! Try again.***')

            if self.checkCoords(oneCoord) and self.checkCoords(twoCoord):
                self.turnCard(oneCoord,twoCoord)
                if self.isGameOver()==True:
                    self.displayBoard()
                    break

    def isGameOver(self):
        winCounter=0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.Dlist[row][column].isFaceUp():
                    winCounter+=1
        if winCounter==self.numCards*2:
            return True
    
    

def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print ("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print ("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print ("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()

if __name__ == "__main__":
    main()
