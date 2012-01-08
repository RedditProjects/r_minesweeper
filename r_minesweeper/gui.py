"""
The GUI Front end of r_minesweeper.

TODO:
    -Dynamically add and remove titles
"""

from Tkinter import *
#seconds, minutes
time = 0

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()
        self.newButton = Button(self, text='New Game')
        self.newButton.grid()
        self.newButton.place()
        self.noMines = Label(self, text='Mines: x/x')
        self.noMines.grid()
        self.time = Label(self, text='Time: 00:00')
        self.time.grid()

    def createGrid(self, noMines):
        for i in range(noMines):
            pass


def Time(self):
    global time
    time += 1
    text = time
    self.time.config(text=text)
    self.time.update_idletasks()

app = Application()
app.pack_propagate(0)
app.master.title("r_Mindsweeper")
app.mainloop()