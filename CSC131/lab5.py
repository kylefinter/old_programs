'''
Kyle Finter
finter179
02/22/2016
GUI convert between Fahrenheit to Celsius and vice versa'''

from tkinter import *

class TemperatureConversion(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Temperature Conversion')
        self.grid()

        self._fahrenheitLabel=Label(self,text='Fahrenheit')
        self._fahrenheitLabel.grid(row=0,column=0)
        self._fahrenheitVar=DoubleVar()
        self._fahrenheitVar.set(32.0)
        self._fahrenheitEntry=Entry(self,textvariable=self._fahrenheitVar)
        self._fahrenheitEntry.grid(row=0,column=1)

        self._celsiusLabel=Label(self,text='Celsius')
        self._celsiusLabel.grid(row=1,column=0)
        self._celsiusVar=DoubleVar()
        self._celsiusVar.set(0.0)
        self._celsiusEntry=Entry(self,textvariable=self._celsiusVar)
        self._celsiusEntry.grid(row=1,column=1)

        self._rightArrow=Button(self,text='>>>>',command=self._fToC)
        self._leftArrow=Button(self,text='<<<<',command=self._cToF)

        self._rightArrow.grid(row=2,column=0)
        self._leftArrow.grid(row=2,column=1)

    def _fToC(self):
        fahrenheit=self._fahrenheitVar.get()

        self._celsiusVar.set((fahrenheit-32)*(5/9))

    def _cToF(self):
        celsius=self._celsiusVar.get()

        self._fahrenheitVar.set((celsius*(9/5))+32)

def main():
    TemperatureConversion().mainloop()

main()
