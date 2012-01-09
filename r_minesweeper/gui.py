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
        self.createBoard()
        self.createWidgets()

    #ToDo: Make board use square blocks.
    def createBoard(self):
        self.board = Canvas()
        #Rectangle co-ordinates are from the bottom left point to the top right point.
        self.board.create_rectangle(2, 265, 379, 2, fill="white")
        self.board.grid()
        #Creating the blocks
        for x in range(6):
            self.board.create_line(53 * (x + 1), 0, 53 * (x + 1), 265, fill="black")
        for x in range(7):
            self.board.create_line(2, 34 * (x + 1), 379, 34 * (x + 1), fill="black")

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


def Time(self):
    global time
    time += 1
    text = time
    self.time.config(text=text)
    self.time.update_idletasks()

app = Application()
app.master.title("r_Mindsweeper")
app.mainloop()
