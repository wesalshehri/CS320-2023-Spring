####################################################
#!/usr/bin/env python3
####################################################
import sys
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
####################################################
"""
HX-2023-03-24: 20 points
Solving the N-queen puzzle
"""
####################################################


def initialize_board(size):
    board = []
    for i in range(size):
        board.append(0)
    return [board]

def is_valid_placement(board, row, col):
    for i in range(row):
        if (board[i] == col or (abs(row - i) == abs(board[i] - col))):
            return False
    return True

def get_children_boards(board, size):
    children = []
    row = 0
    while row < size:
        if board[row] != 0:
            row += 1
        else:
            break
    for col in range(1, size + 1):
        if is_valid_placement(board, row, col):
            new_board = board[:]
            new_board[row] = col
            children.append(new_board)
    return children

def solve_N_queen_puzzle(n):
    initial_board = initialize_board(n)
    search_tree = gtree_dfs(initial_board, lambda board: get_children_boards(board, n))
    valid_boards = stream_make_filter(search_tree, lambda board: tuple(board) if board[-1] != 0 else None)
    return valid_boards



####################################################
