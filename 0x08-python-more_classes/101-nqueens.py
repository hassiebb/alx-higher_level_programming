#!/usr/bin/python3
import sys
''' 
    column first element, row second element
'''
def reject(board):
    for col_A in board:
        for col_B in board:
            if not col_A is col_B:
                if col_A[0] == col_B[0]:
                    return True
                if col_A[1] == col_B[1]:
                    return True
                if col_A[1] - col_A[0] == col_B[1] - col_B[0]:
                    return True
                if col_A[0] + col_A[1] == col_B[0] + col_B[1]:
                    return True
    return False

def accept(board):
    if len(board) < board_size:
        return False
    else: # more tests def needed
        return not(reject(board))

def print_board(board):
    print(str(board))

def first(board):
    # print("DEBUG: def first()")
    # print("pre-board: {}".format(board))
    board.append([len(board), 0])
    # print("post-board: {}".format(board))
    return board

def isdone(board):
    if len(board) == 0:
        return True
    # print("DEBUG: isdone:", end='')
    # print(board[-1][1])
    if board[-1][1] > board_size:
        return True
    else:
        return False

def next_board(board):
    board[-1][1] += 1
    return board

def bt(board):
    # print("DEBUG: huck")
    # print("DEBUG: " + str(board))
    if reject(board):
        # print("DEBUG: {}reject: {}".format(board_size, board))
        return
    if accept(board):
        print_board(board)
    if len(board) < board_size - 1:
        new_board = first(board)
    # print("DEBUG: new_board = {}".format(new_board))
    while not isdone(new_board):
        print("DEBUG: bt() while {}".format(board))
        bt(new_board)
        print("DEBUG: after bt() call")
        new_board = next_board(new_board)

if __name__ == '__main__':
    #one or the other
    if len(sys.argv) >= 2:
        board_size = int(sys.argv[1])
    else:
        raise ValueError("USAGE: ./101-nqueens.py <x>, where x is board size")
    
    bt([])
    # bt([0,0])
         