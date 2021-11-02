import pygame


class Board:
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def check_slot(self, pos, val):
        for i in range(9):
            if pos[0] != i and val == self.board[i][pos[1]]:
                return False
        for j in range(9):
            if pos[1] != j and val == self.board[pos[0]][j]:
                return False
        grid_x = pos[1] // 3
        grid_y = pos[0] // 3

        for i in range(3):
            for j in range(3):
                if pos[0] != grid_y * 3 + i or pos[1] != grid_x * 3 + j:
                    if val == self.board[grid_y * 3 + i][grid_x * 3 + j]:
                        return False
        return True

    def check(self):
        # checking if rows are correct
        for r in range(9):
            row_vals = [False] * 9
            for c in range(9):
                val = self.board[r][c]
                if val != 0:
                    if row_vals[val - 1]:
                        return False
                    else:
                        row_vals[val - 1] = True

        # checking if columns are correct
        for c in range(9):
            column_vals = [False] * 9
            for r in range(9):
                val = self.board[r][c]
                if val != 0:
                    if column_vals[val - 1]:
                        return False
                    else:
                        column_vals[val - 1] = True

        # checking if boxes are correct
        for y in range(3):
            for x in range(3):
                box_vals = [False] * 9
                for r in range(3):
                    for c in range(3):
                        val = self.board[y * 3 + r][x * 3 + c]
                        if val != 0:
                            if box_vals[val - 1]:
                                return False
                            else:
                                box_vals[val - 1] = True
        return True

    def draw(self, win):
        win.fill((255, 255, 255))
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.rect(win, (0, 0, 0), (0, i * 100 - 5, 100 * 9, 10))
            else:
                pygame.draw.rect(win, (0, 0, 0), (0, i * 100 - 5, 100 * 9, 5))
        for j in range(10):
            if j % 3 == 0:
                pygame.draw.rect(win, (0, 0, 0), (j * 100 - 5, 0, 10, 100 * 9))
            else:
                pygame.draw.rect(win, (0, 0, 0), (j * 100 - 5, 0, 5, 100 * 9))
