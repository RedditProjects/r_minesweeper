"""
This is the main source file, and uses the board and gui classes to run.

TODO:
    -add GUI
"""
import board

#Constants:
board_size = 10
num_bombs = 20

bd = board.board(board_size, num_bombs)
bd.print_state(True) # Prints the whole board

while True:
    x = int(input("Enter an x coord (0-9): "))
    y = int(input("Enter a y coord (0-9): "))
    if x >= 0 and x < board_size and y >= 0 and y < board_size:
        if bd.b[y][x].state == -1:
            print("You lose!")
        else:
            bd.unhide([x, y])
            bd.print_state()
    else:
        print("Bad coordinates!")
