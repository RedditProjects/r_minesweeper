"""
This is the board (and tile) class which acts as the board for the game.
The tile class is a container for the tile information.
The board class sets up the board randomly, and initiates itself.

Info:
On the 'board': 0       Empty Square
                1-8     Number of bombs bordering
                -1      Bomb here!
                -2      Hidden tile
"""
from random import *

class tile: # tiles on the board, a small class to hold each tile's status
    def __init__(self, pos):
        self.hidden = True
        self.state = 0
        self.pos = pos #[x, y] coordinate
        
class board: # The board which the game is played on, stores the board itself
             # as well as functions iniating the setup and for printing the
             # state
    def __init__(self, board_size, num_bombs):
        self.board_size = board_size
        self.num_bombs = num_bombs
        self.b = []
        # Fill the board with new tiles
        for y in range(self.board_size):
            temp = []
            for x in range(self.board_size):
                temp.append(tile([x, y]))
            self.b.append(temp)
        # Randomly generate bombs
        self.add_bombs()
        # Add the "number" of each non-bomb tile
        for a in self.b:
            for t in a:
                if t.state != -1:
                    self.set_status(t)

    def add_bombs(self): # Adds bombs randomly
        xy_range = [] # Possible bomb possitions
        for a in range(self.board_size):
            for b in range(self.board_size):
                xy_range.append([b, a])
        for i in range(self.num_bombs):
            new_pos = choice(xy_range)
            self.b[new_pos[1]][new_pos[0]].state = -1
            xy_range.remove(new_pos)

    def set_status(self, t): # Changes each non-bomb tile to the number of bombs
                             # nearby
        n_bombs_near = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                # If the [x, y] coord is on the board:
                if t.pos[0]+x >= 0 and t.pos[0]+x < self.board_size and t.pos[1]+y >= 0 and t.pos[1]+y < self.board_size:
                    if self.b[t.pos[1]+y][t.pos[0]+x].state == -1:
                        n_bombs_near += 1
        t.state = n_bombs_near

    def unhide(self, pos): # Used for unhiding around unhidden empty
                                  # squares
        x = pos[0]
        y = pos[1]
        self.b[y][x].hidden = False
        if self.b[y][x].state == 0: #If it is 0, unhide all tiles around it
            for p in range(-1, 2):
                for q in range(-1, 2):
                    # If the [q, p] coord is on the board:
                    if x+q >= 0 and x+q < self.board_size and y+p >= 0 and y+p < self.board_size:
                        if self.b[y+p][x+q].state == 0 and self.b[y+p][x+q].hidden == True:
                            self.unhide([x+q, y+p])
                        self.b[y+p][x+q].hidden = False
            
        
    def print_state(self, all_unhide=False): # Prints the board
        if all_unhide == True: # Used for printing the entire board
            for i in self.b:
                print([str(a.state).rjust(2) for a in i]) 
        else: # Used for printing only the unhidden tiles
            temp_table = []
            for i in self.b:
                temp_table.append([a for a in i])
            for n in temp_table:
                line = [z for z in n]
                for i in range(len(line)):
                    if line[i].hidden == True:
                        line[i] = -2
                    else:
                        line[i] = line[i].state
                print([str(x).rjust(2) for x in line])
