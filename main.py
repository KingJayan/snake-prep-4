import os
import time
import random as r
import keyboard as key

WIDTH, HEIGHT = 40, 20

snake = [[10,15], [10,14], [10,13]]
food = [5,20]
direction = [0,1] #right

def draw_board():
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    # draw food
    board[food[0]][food[1]] = 'O'
    # draw snake
    for i, segment in enumerate(snake):
        char = 'X' if i == 0 else '#'
        board[segment[0]][segment[1]] = char
    
    # render
    output = "\033[H" + "\n".join("".join(row) for row in board)
    print(output, end="", flush=True)