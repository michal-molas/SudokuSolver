def solve(board):
    empties = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empties.append((i, j))
    current_el = 0
    possibilities = []
    for i in range(len(empties)):
        possibilities.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    while current_el < len(empties):
        print()
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
        for i in range(9):
            print(board[i])


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


b = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if __name__ == "__main__":
    solve(b)
