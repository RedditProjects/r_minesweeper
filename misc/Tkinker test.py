from tkinter import *
from threading import Timer
from time import *

#Constants:
grid_size = 60
size_of_sq = 10
offset = 2
wrap = True

class CGOL:
    def __init__(self, size, sys):
        self.size = size
        self.system = sys

    def step(self):
        newsys = []
        for y in range(len(self.system)):
            new_x_list = []
            for x in range(len(self.system)):
                if self.system[y][x] == 1:
                    new_x_list.append(1)
                else:
                    new_x_list.append(0)
            newsys.append(new_x_list)
        
        for y in range(len(self.system)):
            for x in range(len(self.system)):
                n_living = self.get_live_neighbors([x, y])
                if n_living < 2:
                    newsys[y][x] = 0
                elif n_living > 3:
                    newsys[y][x] = 0
                elif n_living == 3 and self.system[y][x] == 0:
                    newsys[y][x] = 1
        self.system = newsys
        return self.system

    def get_live_neighbors(self, pos): # pos is a list of the format: [x, y]
        ans = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                new_x = pos[0]+x
                new_y = pos[1]+y
                if new_x == -1:
                    new_x = self.size-1
                    if wrap == False: continue
                if new_x == self.size:
                    new_x = 0
                    if wrap == False: continue
                if new_y == -1:
                    new_y = self.size-1
                    if wrap == False: continue
                if new_y == self.size:
                    new_y = 0
                    if wrap == False: continue
                
                if self.system[new_y][new_x] == 1:
                    if new_x != pos[0] or new_y != pos[1]:
                        ans += 1
        return ans
    
    def print_sys(self):
        [print(line) for line in self.system]
        print()

class GUI:
    class Square:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.color = 0 # 1 = black, 0 = white
            self.squareId = 0

        def switch_color(self, canvas):
            if self.color == 1:
                f = '#ffffff'
                self.color = 0
            else:
                f = '#000000'
                self.color = 1
            self.change_color(canvas, f)

        def change_color(self, canvas, f):
            canvas.itemconfigure(self.squareId, fill=f)
            if f == '#ffffff':
                self.color = 0
            else:
                self.color = 1
        
    def __init__(self):
        self.stop = True
        self.frame = Frame()
        self.frame.master.wm_title("Conrads game of life")
        size = grid_size * size_of_sq
        self.canvas = Canvas(self.frame, width = size, height = size)
        self.canvas.pack()

        self.menu_frame = Frame(self.frame)
        self.menu_frame.pack(expand=Y, fill=X)

        #Start Button
        self.start_button = Button(self.menu_frame, text='Go', command=self.start)
        self.start_button.pack(side=LEFT, padx=5)

        #Clear Button
        self.clear_button = Button(self.menu_frame, text='Clear', command=self.clear)
        self.clear_button.pack(side=LEFT, padx=10)

        #Pause Button
        self.pause_button = Button(self.menu_frame, text='Pause', command=self.pause)
        self.pause_button.pack(side=LEFT, padx=5)
        self.pause_button.config(state=DISABLED)

        #Export Config Button
        self.export_button = Button(self.menu_frame, text='Export Config', command=self.export_config)
        self.export_button.pack(side=LEFT, padx=5)

        #Input Entry
        self.e = Entry(self.menu_frame, width = 70)
        self.e.pack()

        #Import Config Button
        self.import_button = Button(self.menu_frame, text='Import Config', command=self.import_config)
        self.import_button.pack(side=LEFT, padx=5)

        self.frame.pack()

        self.squares = []
        for y in range(grid_size):
            new_x_list = []
            for x in range(grid_size):
                new_x_list.append(0)
            self.squares.append(new_x_list)
        
        for x in range(grid_size):
            for y in range(grid_size):
                square = self.squares[y][x] = GUI.Square(x, y)
                x0 = x * size_of_sq + offset
                y0 = y * size_of_sq + offset
                square.squareId = self.canvas.create_rectangle(x0, y0,
                                                               x0+size_of_sq, y0+size_of_sq,
                                                               fill='#ffffff')
                self.canvas.tag_bind(square.squareId, '<ButtonPress>', lambda e, c=self.canvas, sq=square: sq.switch_color(self.canvas))
                
    def start(self):
        self.stop = False
        engine = CGOL(grid_size, self.export_state())
        self.cont = Controller(self, engine)
        self.cont.advance()
        self.start_button.config(state=DISABLED)
        self.clear_button.config(state=DISABLED)
        self.export_button.config(state=DISABLED)
        self.import_button.config(state=DISABLED)
        self.pause_button.config(state=NORMAL)

        for y in range(grid_size):
            for x in range(grid_size):
                self.canvas.tag_unbind(self.squares[y][x].squareId, '<ButtonPress>')

    def pause(self):
        self.stop = True
        self.start_button.config(state=NORMAL)
        self.clear_button.config(state=NORMAL)
        self.export_button.config(state=NORMAL)
        self.import_button.config(state=NORMAL)
        self.pause_button.config(state=DISABLED)

        for y in range(grid_size):
            for x in range(grid_size):
                self.canvas.tag_bind(self.squares[y][x].squareId, '<ButtonPress>', lambda e, c=self.canvas, sq=self.squares[y][x]: sq.switch_color(self.canvas))

        del self.cont

    def clear(self):
        for y in range(grid_size):
            for x in range(grid_size):
                self.squares[y][x].change_color(self.canvas, "#ffffff")

    def export_config(self):
        res = []
        for y in range(len(self.squares)):
            for x in range(len(self.squares)):
                if self.squares[y][x].color == 1:
                    res.append([x, y])
        print(res)

    def import_config(self):
        for y in range(grid_size):
            for x in range(grid_size):
                if self.squares[y][x] == 1:
                    self.squares[y][x] = 0
        last_start = 0
        inp = list(self.e.get())[1:-1]
        for c in range(len(inp)):
            if inp[c] == '[':
                last_start = c
            if inp[c] == ']':
                coord = "".join(inp[last_start + 1 : c]).split(", ")
                for i in range(len(coord)):
                    coord[i] = int(coord[i])
                self.squares[coord[1]][coord[0]].change_color(self.canvas, '#000000')
            

    def export_state(self):
        system = []
        for y in range(grid_size):
            new_x_list = []
            for x in range(grid_size):
                new_x_list.append(0)
            system.append(new_x_list)
            
        for y in range(grid_size):
            for x in range(grid_size):
                if self.squares[y][x].color == 1:
                    system[y][x] = 1
        return system

    def change_state(self, new_state):
        for y in range(grid_size):
            for x in range(grid_size):
                if self.squares[y][x].color == new_state[y][x]:
                    continue
                if new_state[y][x] == 0:
                    f = "#ffffff"
                elif new_state[y][x] == 1:
                    f = "#000000"
                self.squares[y][x].change_color(self.canvas, f)

class Controller:
    def __init__(self, view, engine):
        self.gui = view
        self.engine = engine

    def advance(self):
        if self.gui.stop == False:
            self.gui.change_state(self.engine.step())
            t = Timer(0.0001, self.advance)
            t.start()


gui = GUI()
gui.frame.mainloop()
