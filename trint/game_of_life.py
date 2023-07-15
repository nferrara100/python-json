# Create grid
size = 10
grid = [[False for x in range(0, size)] for y in range(0, size)]

# Default data
grid[4][5] = True
grid[4][6] = True
grid[4][7] = True
grid[4][8] = True
grid[3][4] = True
grid[3][5] = True
grid[3][9] = True
grid[5][5] = True
grid[5][7] = True


# Refresh grid
def tick():
    living = 0
    changes = 0
    for y in range(0, size):
        for x in range(0, size):
            cell = grid[y][x]
            neighbors = 0
            try:
                if grid[y - 1][x] is True:
                    neighbors += 1
                if grid[y + 1][x] is True:
                    neighbors += 1
                if grid[y][x - 1] is True:
                    neighbors += 1
                if grid[y][x + 1] is True:
                    neighbors += 1
            except IndexError:
                pass

            if cell is False and neighbors == 3:
                cell = True
                changes += 1
            if cell is True and (neighbors < 2 or neighbors > 3):
                cell = False
                changes += 1

            if cell is True:
                print("🐒", end="")
                living += 1
            else:
                print("⬜", end="")
        print("")

    if living > 0 and changes > 0:
        print("")
        tick()


# Start simulation
tick()
