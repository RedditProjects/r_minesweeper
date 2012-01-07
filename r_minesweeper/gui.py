"""
The GUI Front end of r_minesweeper.

TODO:
    -Dynamically add and remove titles
"""

from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        ##self.menubar = Menu(self)
        ##self.menubar.add_command(label='New Game')
        ##self.menubar.add_command(label='Quit')
        ##self.config(menu=menubar)
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


app = Application()
app.pack_propagate(0)
app.master.title("r_Mindsweeper")
app.mainloop()