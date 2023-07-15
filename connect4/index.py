def check_grid(grid, x, y):
    last = 0
    streak = 0
    for cell in grid[y]:
        if last == 1 and cell == 1:
            streak += 1
        if last == 2 and cell == 2:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            return cell
        last = cell


def check_grid_vert(grid, x, y):
    last = 0
    streak = 0
    for row in grid:
        cell = row[x]
        if last == 1 and cell == 1:
            streak += 1
        if last == 2 and cell == 2:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            return cell
        last = cell


def check_grid_di(grid, x, y):
    last = 0
    streak = 0

    di_list = [grid[y, x]]
    for inc in range(0, 6):
        try:
            di_list.append(grid[x + inc, y + inc])
        except Exception:
            break

    for row in grid:
        cell = row[x]
        if last == 1 and cell == 1:
            streak += 1
        if last == 2 and cell == 2:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            return cell
        last = cell
