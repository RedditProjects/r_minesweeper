from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

app = Application()
app.pack_propagate(0)
app.master.title("r_Mindsweeper")
app.mainloop()