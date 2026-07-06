import os
import time
import random as r
import keyboard as key

WIDTH, HEIGHT = 40, 20

snake = [[10,15], [10,14], [10,13]] # 3 vertical pixels of the snake
food = [5,20]
direction = [0,1] #right

def draw_board():
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)] # makes the board a 2d array for spaces
    # draw food
    board[food[0]][food[1]] = 'O' # sets all food characters to 'O'
    # draw snake
    for i, segment in enumerate(snake):
        char = 'X' if i == 0 else '#' # sets the head of the snake to 'X' and the rest of the body to '#'
        board[segment[0]][segment[1]] = char # sets the snake segments to the appropriate character
    
    # render
    output = "\033[H" + "\n".join("".join(row) for row in board) # joins the rows of the board into a single string
    print(output, end="", flush=True)

os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal screen
print("\033[?25l", end="") # hide cursor

while True:
    # keyboard input handling

    # calculate new head position per-frame

    # collision conditions (runs into self, runs into wall)

    # logic after eating food (grow snake, spawn new food)

    break

# game over + restore cursor