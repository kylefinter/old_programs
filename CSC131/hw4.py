"""
Sample solution for HW3 - Memory Matching Game
Author: Jamil Saquer
Date: February, 2016
"""
import random
from tkinter import *

class Card(object):
    """ A card object with a suit and rank."""

    def __init__(self, rank):
        """Creates a card with the given rank and face down."""
        self.rank = rank
        self.face = 'down'

    def getFace(self):
        return self.face

    def setFace(self, value):
        """show face up or down"""
        self.face = value
        
    def __str__(self):
        """Returns the string representation of a card."""
        return str(self.rank)

#----------------------------------
    
class Deck(object):
    """ A deck containing numberOfPairs pairs of identical cards."""

    def __init__(self, numberOfPairs):
        """Creates a deck of numberOfPairs pairs of identical cards."""
        self._cards = []
        for rank in range(1, numberOfPairs + 1): #start by 1 (not 0) as first rank
            c1 = Card(rank)
            self._cards.append(c1)
            c2 = Card(rank)
            self._cards.append(c2)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self._cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self._cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ''
        for c in self._cards:
            result = result + str(c) + '\n'
        return result

#-----------------------------
    
class Game(Frame):
    """A class that simulates a memory matching game """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid =[]
        
    def play(self):
        """ Simulates playing a game"""
        self.populateGrid()
        self.displayGrid()
        while not self.isGameOver():
            x1, y1 = self.getCoordinates(1)   #input("Enter coordinates of first card ")
            card1 = self.grid[x1 - 1][y1 - 1]
            x2, y2 = self.getCoordinates(2)  #input("Enter coordinates of second card ")
            card2 = self.grid[x2 - 1][y2 - 1]
            if (x1, y1) == (x2, y2): #coordinates must be different for the two cards
                print("    ***Coordinates for the two cards must be different, try again***")
                continue #continue with while loop
            if card1.rank == card2.rank: #an identical pair
                #print('identical pair')
                card1.face = 'up'
                card2.face = 'up'
            else:
                print("    Not an identical pair. Found %d at (%d,%d) and %d at (%d,%d)" \
                      % (card1.rank, x1, y1, card2.rank, x2, y2))
            self.displayGrid()
            
    def getCoordinates(self, cardNumber):
        """Get valid card's coordinates from user"""
        number = 'first' if cardNumber == 1 else 'second'
        while True:
            s = input("Enter coordinates for " + number + " card ")
            s = s.strip()
            x = s[0]
            y = s[-1]
            if x.isdigit() and y.isdigit():
                x = int(x)
                y = int(y)
                if 1 <= x <= self.rows and 1 <= y <= self.columns:
                    return x, y
                else:
                    print("    ***Invalid coordinates! Try again.***")
            else:
                print("    ***Invalid coordinates! Try again.***")
            

    def isGameOver(self):
        """ retuns True if game is over and False otherwise"""
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j].face == 'down':
                    return False
        #if here then all cards must be face up
        return True

    def populateGrid(self):
        """populate the grid with cards"""
        numberOfPairs = self.rows * self.columns // 2
        deck = Deck(numberOfPairs)
        deck.shuffle()
        #fill grid with cards
        for row in range(self.rows):
            oneRow = self.getOneRow(deck)
            self.grid.append(oneRow)

    def getOneRow(self, deck):
        """return a list of self.columns cards"""
        currentRow = []
        for i in range(self.columns):
            card = deck.deal()
            currentRow.append(card) 
        return currentRow

    def displayGrid(self):
        """Display the grid"""
        for i in range(self.rows):
            for j in range(self.columns):
                upOrDown = self.grid[i][j].face
                if upOrDown == 'up':
                    print(self.grid[i][j], end = " ")
                else: #face is down, so display *
                    print('*', end = " ") 
            print()

class GameGUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Memory Matching Game')
        self.grid()
        self._rowLabel=Label(self,text='Number of rows')
        self._rowLabel.grid(row=0,column=0)
        self._columnLabel=Label(self,text='Number of columns')
        self._columnLabel.grid(row=0,column=2)
        
        self._rowVar=IntVar()
        self._rowVar.set(2)
        self._rowEntry=Entry(self,textvariable=self._rowVar)
        self._rowEntry.grid(row=0,column=1)
        self._columnVar=IntVar()
        self._columnVar.set(2)
        self._columnEntry=Entry(self,textvariable=self._columnVar)
        self._columnEntry.grid(row=0,column=3)
        
        self._newGameButton=Button(self,text='New Game',command=self._newGame)
        self._newGameButton.grid(row=1,column=0,columnspan=2)

        #self._turnOverButton=Button(self,text='Turn Over',command=self._turnOver)
        #self._turnOverButton.grid(row=1,column=2,columnspan=2)
        

    def _newGame(self):
        #check if row * column is odd or greater than 20
        if ((self._rowVar*self._columnVar)%2)==0:# and ((self._rowVar*self._columnVar)//2)<=20:
            game = Game(self._rowVar.get(), self._columnVar.get())
            game.play()
        else:
            #error checking
            pass
        

    #def _turnOver(self):
        
            
def main():
    g=GameGUI()
    '''while True:
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
'''
    

if __name__ == "__main__":
    main()
