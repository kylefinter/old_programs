"""
HW4 - GUI Memory Matching Game
Author: Kyle Finter
Date: 03/17/16
"""
import random
from tkinter import *


class Card(object):
    """ A card object with a suit and rank."""

    def __init__(self, rank, suit):
        """Creates a card with the given rank and face down."""
        self.rank = rank
        self.suit = suit
        self.face = 'down'
        self.fileName ='D:/CSC-131/DECK/'+str(rank)+str(suit)+'.gif'
        
    def getFace(self):
        return self.face

    def setFace(self, value):
        """show face up or down"""
        self.face = value
        
    def __str__(self):
        """Returns the string representation of a card."""
        return str(self.rank)+str(self.suit)

#----------------------------------
    
class Deck(object):
    """ A deck containing numberOfPairs pairs of identical cards."""

    def __init__(self, numberOfPairs):
        """Creates a deck of numberOfPairs pairs of identical cards."""
        self._cards = []
        self._suitList=['s','h','d','c']
        for rank in range(1, numberOfPairs + 1): #start by 1 (not 0) as first rank
            suit=random.choice(self._suitList)
            c1 = Card(rank,suit)
            self._cards.append(c1)
            c2 = Card(rank,suit)
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
    def __init__(self):
        frame = Frame.__init__(self)
        self.master.title("Memory Matching Game")
        self.grid()

        self._widthLabel = Label(self, text = "Number of rows")
        self._widthLabel.grid(row= 0, column =0)

        self._widthVar = IntVar(value = '2')
        self._widthEntry=Entry(self, textvariable = self._widthVar)
        self._widthEntry.grid(row = 0,column = 1)

        self._lengthLabel = Label(self, text = "Number of columns")
        self._lengthLabel.grid(row= 0, column = 2)

        self._lengthVar = IntVar(value = '2')
        self._lengthEntry=Entry(self, textvariable = self._lengthVar)
        self._lengthEntry.grid(row = 0,column = 3)

        newGame = Button(self, text = "New Game", command = self.processNewGame)
        newGame.grid(row = 1, column = 0,columnspan=2)
        turnOver = Button(self, text = "Turn Over", command=self.turnOver)
        turnOver.grid(row = 1, column = 2,columnspan=2)

        self.rowVar=self._widthVar
        self.columnVar=self._lengthVar

        self.photos = [] # List of photo images for the card labels
        self.cards = []  # List of cards to be shown on labels
        self.labels = [] # List of cards' Labels

    def processNewGame(self):
        self.photos = []
        self.cards = []
        self.labels = []
        num = self._widthVar.get() * self._lengthVar.get()
        if num >20:
            messagebox.showerror("Error", "Number of rows X number of columns cannot exceed 20")
        if not (num % 2 == 0):
            messagebox.showerror("Error", "Number of rows X columns must be even")
        elif num<=20 and num%2==0:
            self.play()

    def turnOver(self):
        for i in range(len(self.cards)):
            if self.cards[i].face=='up':
                self.cards[i].face='down'
            else:
                self.cards[i].face='up'
        self.displayGrid()
        
    def play(self):
        """ Simulates playing a game"""
        self.populateGrid()
        self.displayGrid()

    def populateGrid(self):
        """populate the grid with cards"""
        numberOfPairs = self.rowVar.get() * self.columnVar.get() // 2
        deck = Deck(numberOfPairs)
        deck.shuffle()
        i = 0
        for r in range(self.rowVar.get()):
            for c in range(self.columnVar.get()):
                card = deck.deal()
                self.cards.append(card)
                self.photos.append(PhotoImage(file = card.fileName))
                self.labels.append(Label(self, image = self.photos[i]))
                self.labels[i].grid(row = r+2, column = c,ipadx=5,ipady=5)
                self.labels[i].bind("<Button-1>",lambda event, whichCard = i: self._flipCard(event, whichCard))
                i+=1

    def _flipCard(self,event,cardNumber):
        if self.cards[cardNumber].getFace()=='down':
            self.cards[cardNumber].setFace('up')
            self.displayGrid()
        else:
            self.cards[cardNumber].setFace('down')
            self.displayGrid()

    def displayGrid(self):
        """Display the grid"""
        i=0
        for r in range(self.rowVar.get()):
            for c in range(self.columnVar.get()):
                upOrDown = self.cards[i].face
                if upOrDown == 'up':
                    self.photos[i]=PhotoImage(file=str(self.cards[i].fileName))
                    self.labels[i]=Label(self,image=self.photos[i])
                    self.labels[i].grid(row=r+2,column=c,ipadx=5,ipady=5)
                    self.labels[i].bind("<Button-1>",lambda event, whichCard = i: self._flipCard(event, whichCard))
                else: #face is down, so display *
                    self.photos[i]=PhotoImage(file='D:/CSC-131/DECK/b.gif')
                    self.labels[i]=Label(self,image=self.photos[i])
                    self.labels[i].grid(row=r+2,column=c,ipadx=5,ipady=5)
                    self.labels[i].bind("<Button-1>",lambda event, whichCard = i: self._flipCard(event, whichCard))
                i+=1
            
def main():
    Game().mainloop()
   
if __name__ == "__main__":
    main()
