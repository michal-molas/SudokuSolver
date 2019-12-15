import pygame


def run():
    correct = []
    started = [False]
    solved = [False]
    pygame.init()
    win = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("SudokuSolver")

    font = pygame.font.Font('freesansbold.ttf', 64)

    picked = [-1, -1]

    current_slot = [0, 0]
    current_el = [0]
    empties = []
    possibilities = []

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(120)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        update(board, started, events, picked, current_slot, empties, current_el, possibilities, solved, correct)
        draw(win, board, picked, font, started, current_slot)


def check_slot(board, pos, val):
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


def check_board(board, correct):
    for i in range(9):
        vals = {0: -10, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for j in range(9):
            vals[board[i][j]] += 1
        for v in vals.values():
            if v > 1:
                correct.append(False)
                print("Incorrect board :(")
                return
    for i in range(9):
        vals = {0: -10, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for j in range(9):
            vals[board[j][i]] += 1
        for v in vals.values():
            if v > 1:
                correct.append(False)
                print("Incorrect board!")
                return
    for y in range(3):
        for x in range(3):
            vals = {0: -10, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for i in range(3):
                for j in range(3):
                    vals[board[y * 3 + i][x * 3 + j]] += 1
            for v in vals.values():
                if v > 1:
                    correct.append(False)
                    print("Incorrect board!")
                    return
    correct.append(True)


def draw_board(win):
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


def set_picked(events, picked):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            picked[0] = mouse_pos[0] // 100
            picked[1] = mouse_pos[1] // 100


def move_picked(events, picked):
    if picked != [-1, -1]:
        for event in events:
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
                    picked[0] += keys_x[event.key]
                    picked[0] = max(0, picked[0])
                    picked[0] = min(8, picked[0])
                if event.key in keys_y:
                    picked[1] += keys_y[event.key]
                    picked[1] = max(0, picked[1])
                    picked[1] = min(8, picked[1])


def draw_picked(win, picked):
    if picked != [-1, -1]:
        x_pos = picked[0] * 100
        y_pos = picked[1] * 100
        width = 95
        height = 95
        if picked[0] % 3 == 0:
            x_pos += 5
            width -= 5
        if picked[1] % 3 == 0:
            y_pos += 5
            height -= 5

        pygame.draw.rect(win, (150, 150, 150), (x_pos, y_pos, width, height))


def draw_nums(win, board, font):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num_text = font.render(str(board[i][j]), True, (0, 0, 0))
                text_rect = num_text.get_rect()
                text_rect.center = (j * 100 + 50, i * 100 + 50)
                win.blit(num_text, text_rect)


def set_num(events, board, picked):
    if picked != [-1, -1]:
        for event in events:
            if event.type == pygame.KEYDOWN:
                nums = {
                    pygame.K_1: 1,
                    pygame.K_2: 2,
                    pygame.K_3: 3,
                    pygame.K_4: 4,
                    pygame.K_5: 5,
                    pygame.K_6: 6,
                    pygame.K_7: 7,
                    pygame.K_8: 8,
                    pygame.K_9: 9,
                    pygame.K_DELETE: 0,
                    pygame.K_BACKSPACE: 0
                }
                if event.key in nums.keys():
                    board[picked[1]][picked[0]] = nums[event.key]


def run_solver(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                return True
    return False


def draw_current_slot(win, current_slot):
    x_pos = current_slot[0] * 100
    y_pos = current_slot[1] * 100
    width = 95
    height = 95
    if current_slot[0] % 3 == 0:
        x_pos += 5
        width -= 5
    if current_slot[1] % 3 == 0:
        y_pos += 5
        height -= 5

    pygame.draw.rect(win, (0, 200, 0), (x_pos, y_pos, width, height))


def set_empties(board, empties):
    if len(empties) == 0:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    empties.append((i, j))


def set_possibilities(empties, possibilities):
    if len(possibilities) == 0:
        for i in range(len(empties)):
            possibilities.append([1, 2, 3, 4, 5, 6, 7, 8, 9])


def solve_step(board, empties, current_el, possibilities, solved, current_slot, correct):
    if not check_slot(board, empties[current_el[0]], possibilities[current_el[0]][0]):
        if len(possibilities[current_el[0]]) > 1:
            possibilities[current_el[0]].pop(0)
        else:
            while len(possibilities[current_el[0]]) == 1:
                board[empties[current_el[0]][0]][empties[current_el[0]][1]] = 0
                possibilities[current_el[0]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                current_el[0] -= 1
            possibilities[current_el[0]].pop(0)
    else:
        board[empties[current_el[0]][0]][empties[current_el[0]][1]] = possibilities[current_el[0]][0]
        current_el[0] += 1
        if current_el[0] == len(empties):
            current_slot[1] = -1
            current_slot[0] = -1
            solved[0] = True
            print("Finished!")
    if len(possibilities[0]) == 0:
        correct[0] = False
        print("Unsolvable board :(")


def update(board, started, events, picked, current_slot, empties, current_el, possibilities, solved, correct):
    if not solved[0]:
        if started[0]:
            if len(correct) == 0:
                check_board(board, correct)
            set_empties(board, empties)
            set_possibilities(empties, possibilities)
            if current_el[0] < len(empties) and correct[0]:
                current_slot[1] = empties[current_el[0]][0]
                current_slot[0] = empties[current_el[0]][1]
                solve_step(board, empties, current_el, possibilities, solved, current_slot, correct)
        else:
            set_picked(events, picked)
            move_picked(events, picked)
            set_num(events, board, picked)
            if run_solver(events):
                started[0] = True


def draw(win, board, picked, font, started, current_slot):
    draw_board(win)
    if not started[0]:
        draw_picked(win, picked)
    else:
        draw_current_slot(win, current_slot)
    draw_nums(win, board, font)

    pygame.display.update()
