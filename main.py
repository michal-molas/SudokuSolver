import copy
from gui import *


def solve(board):
    solvable = True
    empties = []
    in_board = copy.deepcopy(board)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empties.append((i, j))
    current_el = 0
    possibilities = []
    for i in range(len(empties)):
        possibilities.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    while current_el < len(empties):
        if not check(board, empties[current_el], possibilities[current_el][0]):
            if len(possibilities[current_el]) > 1:
                possibilities[current_el].pop(0)
            else:
                while len(possibilities[current_el]) == 1:
                    board[empties[current_el][0]][empties[current_el][1]] = 0
                    possibilities[current_el] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    current_el -= 1
                possibilities[current_el].pop(0)
        else:
            board[empties[current_el][0]][empties[current_el][1]] = possibilities[current_el][0]
            current_el += 1
        if len(possibilities[0]) == 0:
            solvable = False
            print("Unsolvable board!")
    if solvable:
        print("Input board:")
        for i in range(9):
            for j in range(9):
                print(in_board[i][j], end=" ")
                if j == 2 or j == 5:
                    print("|", end=" ")
            print()
            if i == 2 or i == 5:
                print("---------------------")
        print()
        print("Solved board:")
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
                if j == 2 or j == 5:
                    print("|", end=" ")
            print()
            if i == 2 or i == 5:
                print("---------------------")


def check(board, pos, val):
    for i in range(9):
        if pos[0] != i and val == board[i][pos[1]]:
            return False
    for j in range(9):
        if pos[1] != j and val == board[pos[0]][j]:
            return False
    grid_x = pos[1] // 3
    grid_y = pos[0] // 3

    for i in range(3):
        for j in range(3):
            if pos[0] != grid_y * 3 + i or pos[1] != grid_x * 3 + j:
                if val == board[grid_y * 3 + i][grid_x * 3 + j]:
                    return False
    return True


b1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

b2 = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 4, 3, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 6],
      [0, 0, 0, 5, 0, 9, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 4, 1, 8],
      [0, 0, 0, 0, 8, 1, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0, 5, 0],
      [0, 4, 0, 0, 0, 0, 3, 0, 0]]

b3 = [[8, 0, 0, 7, 0, 0, 0, 5, 0],
      [0, 0, 9, 0, 0, 5, 0, 4, 0],
      [0, 0, 3, 0, 0, 8, 0, 0, 0],
      [0, 3, 0, 0, 0, 4, 0, 0, 6],
      [7, 0, 0, 0, 0, 0, 0, 0, 8],
      [4, 0, 0, 9, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0, 0, 2, 0, 0],
      [0, 5, 0, 4, 0, 0, 9, 0, 0],
      [0, 8, 0, 0, 0, 7, 0, 0, 5]]

b4 = [[0, 0, 4, 0, 3, 0, 6, 0, 0],
      [0, 0, 7, 0, 0, 4, 3, 0, 0],
      [0, 0, 0, 8, 0, 1, 9, 0, 0],
      [0, 9, 0, 7, 0, 5, 0, 1, 0],
      [7, 0, 3, 2, 0, 0, 0, 6, 0],
      [5, 0, 0, 0, 0, 0, 0, 0, 0],
      [4, 0, 0, 0, 6, 0, 0, 0, 0],
      [3, 0, 0, 0, 2, 0, 5, 9, 0],
      [2, 0, 5, 0, 0, 0, 0, 8, 0]]


if __name__ == "__main__":
    run()
    #solve(b4)
