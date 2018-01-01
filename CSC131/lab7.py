'''
Kyle Finter
finter179
3/17/16
lab7 GUI program to draw rectangle and an oval with checkbox to determine if it should be filled'''
from tkinter import *

class DrawRectangleOval(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("GUIs drawing geomatric shapes")
        self.grid()

        self.canvas=Canvas(self,bg='white',width=400,height=300)
        self.canvas.grid()

        frame1=Frame(self)
        frame1.grid()
        self.v1=IntVar(value=0)
        rectangleRadio=Radiobutton(frame1,text='Rectangle',variable=self.v1,
                                   value=1,command=self.drawRectangle)
        rectangleRadio.grid(row=0,column=0)

        ovalRadio=Radiobutton(frame1,text='Oval',variable=self.v1,
                              value=2,command=self.drawOval)
        ovalRadio.grid(row=0,column=1)

        self.v2=IntVar(value=0)
        filledButton=Checkbutton(frame1,text='Filled',variable=self.v2,
                                      onvalue=1,offvalue=0)
        filledButton.grid(row=0,column=2)

        clearButton=Button(frame1,text='Clear',command=self.clearCanvas)
        clearButton.grid(row=0,column=3)

    def drawRectangle(self):
        if self.v2.get()==0:
            self.canvas.create_rectangle(50,50,250,250,tags='rect')
        else:
            self.canvas.create_rectangle(50,50,250,250,tags='rect',fill='red')

    def drawOval(self):
        if self.v2.get()==0:
            self.canvas.create_oval(50,100,250,200,tags='oval')
        else:
            self.canvas.create_oval(50,100,250,200,tags='oval',fill='yellow')

    def clearCanvas(self):
        self.canvas.delete('rect','oval')

def main():
    DrawRectangleOval().mainloop()
main()
