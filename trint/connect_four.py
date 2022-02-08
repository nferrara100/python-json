grid = [[0 for y in range(0, 7)] for x in range(0, 6)]

for x in range(0, 6):
    for y in range(0, 7):
        cell = grid[x][y]
        if cell == 0:
            print("⬜", end="")
        if cell == 1:
            print("🟥", end="")
        if cell == 2:
            print("🟩", end="")
    print("")


def has_won(grid_state):
    for x in range(0, 6):
        num_in_row_1 = 0
        num_in_row_2 = 0
        for y in range(0, 7):
            if grid[x][y] == 1:
                num_in_row_1 += 1
                num_in_row_2 = 0
            elif grid[x][y] == 2:
                num_in_row_2 += 1
                num_in_row_1 = 0
            elif grid[x][y] == 0:
                num_in_row_2 = 0
                num_in_row_1 = 0
        if num_in_row_1 > 3:
            return 1
        if num_in_row_2 > 3:
            return 2
    return 0
