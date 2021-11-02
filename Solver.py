from Board import *


class Solver:
    def __init__(self):
        self.started = False
        self.solved = False
        self.correct = False
        self.board = Board()

        self.num_keys = {
            pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 4,
            pygame.K_5: 5,
            pygame.K_6: 6,
            pygame.K_7: 7,
            pygame.K_8: 8,
            pygame.K_9: 9,
            pygame.K_KP1: 1,
            pygame.K_KP2: 2,
            pygame.K_KP3: 3,
            pygame.K_KP4: 4,
            pygame.K_KP5: 5,
            pygame.K_KP6: 6,
            pygame.K_KP7: 7,
            pygame.K_KP8: 8,
            pygame.K_KP9: 9,
            pygame.K_DELETE: 0,
            pygame.K_BACKSPACE: 0
        }

        self.win = None
        self.font = None

        self.picked = [-1, -1]

        self.current_slot = [0, 0]
        self.current_el = [0]
        self.empties = []
        self.possibilities = []

        self.events = None

    def run(self):
        pygame.init()
        self.win = pygame.display.set_mode((900, 900))
        pygame.display.set_caption("SudokuSolver")
        self.font = pygame.font.Font('freesansbold.ttf', 64)

        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(120)
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    running = False
            if not self.update():
                break
            self.draw()
        pygame.quit()

    def update(self):
        if not self.solved:
            if self.started:
                if not self.correct:
                    print("Board is unsolvable :(")
                    return False
                self.set_empties()
                self.set_possibilities()
                if self.current_el[0] < len(self.empties):
                    self.current_slot[1] = self.empties[self.current_el[0]][0]
                    self.current_slot[0] = self.empties[self.current_el[0]][1]
                    self.solve_step()
            else:
                self.set_picked()
                self.move_picked()
                self.set_num()
                if self.run_solver():
                    self.started = True
                    self.correct = self.board.check()
        return True

    def draw(self):
        self.board.draw(self.win)
        if not self.started:
            self.draw_picked()
        else:
            self.draw_current_slot()
        self.draw_nums()

        pygame.display.update()

    def set_picked(self):
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                self.picked[0] = mouse_pos[0] // 100
                self.picked[1] = mouse_pos[1] // 100

    def move_picked(self):
        if self.picked != [-1, -1]:
            for event in self.events:
                if event.type == pygame.KEYDOWN:
                    keys_x = {
                        pygame.K_d: 1,
                        pygame.K_RIGHT: 1,
                        pygame.K_a: -1,
                        pygame.K_LEFT: -1
                    }
                    keys_y = {
                        pygame.K_s: 1,
                        pygame.K_DOWN: 1,
                        pygame.K_w: -1,
                        pygame.K_UP: -1
                    }
                    if event.key in keys_x:
                        self.picked[0] += keys_x[event.key]
                        self.picked[0] = max(0, self.picked[0])
                        self.picked[0] = min(8, self.picked[0])
                    if event.key in keys_y:
                        self.picked[1] += keys_y[event.key]
                        self.picked[1] = max(0, self.picked[1])
                        self.picked[1] = min(8, self.picked[1])

    def draw_picked(self):
        if self.picked != [-1, -1]:
            x_pos = self.picked[0] * 100
            y_pos = self.picked[1] * 100
            width = 95
            height = 95
            if self.picked[0] % 3 == 0:
                x_pos += 5
                width -= 5
            if self.picked[1] % 3 == 0:
                y_pos += 5
                height -= 5

            pygame.draw.rect(self.win, (150, 150, 150), (x_pos, y_pos, width, height))

    def draw_nums(self):
        for i in range(9):
            for j in range(9):
                if self.board.board[i][j] != 0:
                    num_text = self.font.render(str(self.board.board[i][j]), True, (0, 0, 0))
                    text_rect = num_text.get_rect()
                    text_rect.center = (j * 100 + 50, i * 100 + 50)
                    self.win.blit(num_text, text_rect)

    def set_num(self):
        if self.picked != [-1, -1]:
            for event in self.events:
                if event.type == pygame.KEYDOWN:
                    if event.key in self.num_keys.keys():
                        self.board.board[self.picked[1]][self.picked[0]] = self.num_keys[event.key]

    def run_solver(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return True
        return False

    def draw_current_slot(self):
        x_pos = self.current_slot[0] * 100
        y_pos = self.current_slot[1] * 100
        width = 95
        height = 95
        if self.current_slot[0] % 3 == 0:
            x_pos += 5
            width -= 5
        if self.current_slot[1] % 3 == 0:
            y_pos += 5
            height -= 5

        pygame.draw.rect(self.win, (0, 200, 0), (x_pos, y_pos, width, height))

    def set_empties(self):
        if len(self.empties) == 0:
            for i in range(9):
                for j in range(9):
                    if self.board.board[i][j] == 0:
                        self.empties.append((i, j))

    def set_possibilities(self):
        if len(self.possibilities) == 0:
            for i in range(len(self.empties)):
                self.possibilities.append([n + 1 for n in range(9)])

    def solve_step(self):
        pos = self.empties[self.current_el[0]]
        val = self.possibilities[self.current_el[0]][0]
        if not self.board.check_slot(pos, val):
            if len(self.possibilities[self.current_el[0]]) > 1:
                self.possibilities[self.current_el[0]].pop(0)
            else:
                while len(self.possibilities[self.current_el[0]]) == 1:
                    self.board.board[pos[0]][pos[1]] = 0
                    self.possibilities[self.current_el[0]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.current_el[0] -= 1
                self.possibilities[self.current_el[0]].pop(0)
        else:
            self.board.board[pos[0]][pos[1]] = val
            self.current_el[0] += 1
            if self.current_el[0] == len(self.empties):
                self.current_slot[1] = -1
                self.current_slot[0] = -1
                self.solved = True
                print("Finished!")
        if len(self.possibilities[0]) == 0:
            self.correct = False


