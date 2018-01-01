'''
Kyle Finter
finter179
3/3/16
GUI based random card program'''
import random
from tkinter import *

class CardGUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Random Images')
        self.grid()
        self._backImage=PhotoImage(file='DECK/b.gif')
        self._cardImage=self._backImage
        self._imageLabel=Label(self,image=self._cardImage)
        self._imageLabel.grid(row=0,column=0,rowspan=3)
        self._randomButton=Button(self,text='Show Random Card',command=self._shuffle)
        self._randomButton.grid(row=1,column=1)

        self._suitList=['s','h','d','c']

    def _shuffle(self):
        rank=random.randrange(1,14)
        suit=random.choice(self._suitList)
        self._cardImage=PhotoImage(file='DECK/'+str(rank)+suit+'.gif')
        self._imageLabel['image']=self._cardImage

def main():
    CardGUI().mainloop()
main()
