"""
This is a quickly (and poorly) created game.
Info:
On the 'board': 0       Empty Square
                1-8     Number of bombs bordering
                -1      Bomb here!
                -2      Hidden tile

TODO:
    -add adjacent blank tiles to become unhidden
    -loop the UI
    -make code better
"""
from random import *

#Constants:
board_size = 10
num_bombs = 20

class tile: # tiles on the board, a small class to hold each tile's status
    def __init__(self, pos):
        self.hidden = True
        self.state = 0
        self.pos = pos #[x, y] coordinate
        
class board: # The board which the game is played on, stores the board itself
             # as well as functions iniating the setup and for printing the
             # state
    def __init__(self, size):
        self.b = []
        # Fill the board with new tiles
        for y in range(board_size):
            temp = []
            for x in range(board_size):
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
        for a in range(board_size):
            for b in range(board_size):
                xy_range.append([b, a])
        for i in range(num_bombs):
            new_pos = choice(xy_range)
            self.b[new_pos[1]][new_pos[0]].state = -1
            xy_range.remove(new_pos)

    def set_status(self, t): # Changes each non-bomb tile to the number of bombs
                             # nearby
        n_bombs_near = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                # If the [x, y] coord is on the board:
                if t.pos[0]+x >= 0 and t.pos[0]+x < board_size and t.pos[1]+y >= 0 and t.pos[1]+y < board_size:
                    if self.b[t.pos[1]+y][t.pos[0]+x].state == -1:
                        n_bombs_near += 1
        t.state = n_bombs_near

    def print_state(self, all_unhide=False): # Prints the board
        if all_unhide == True: # Used for printing the entire board
            for i in self.b:
                print([a.state for a in i])
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
                print(line)


bd = board(board_size)
bd.print_state(True) # Prints the whole board
# TODO: This needs to be looped, tested, and finalized, I just threw this
# together.
x = int(input("Enter an x coord: "))
y = int(input("Enter a y coord: "))
if x >= 0 and x < board_size and y >= 0 and y < board_size:
    if bd.b[y][x].state == -1:
        print("You lose!")
    else:
        bd.b[y][x].hidden = False
        bd.print_state()
