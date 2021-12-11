def flash(current_row, current_column):
    up = current_row - 1
    right = current_column + 1
    down = current_row + 1
    left = current_column - 1

    # east
    if right < n_columns:
        if (current_row, right) not in seen and rows[current_row][right] + 1 > 9:
            seen.append((current_row, right))
            flash(current_row, right)
        else:
            rows[current_row][right] += 1

    # north-east
    if right < n_columns and up >= 0:
        if (up, right) not in seen and rows[up][right] + 1 > 9:
            seen.append((up, right))
            flash(up, right)
        else:
            rows[up][right] += 1

    # north
    if up >= 0:
        if (up, current_column) not in seen and rows[up][current_column] + 1 > 9:
            seen.append((up, current_column))
            flash(up, current_column)
        else:
            rows[up][current_column] += 1

    # north-west
    if up >= 0 and left >= 0:
        if (up, left) not in seen and rows[up][left] + 1 > 9:
            seen.append((up, left))
            flash(up, left)
        else:
            rows[up][left] += 1

    # west
    if left >= 0:
        if (current_row, left) not in seen and rows[current_row][left] + 1 > 9:
            seen.append((current_row, left))
            flash(current_row, left)
        else:
            rows[current_row][left] += 1

    # south-west
    if left >= 0 and down < n_rows:
        if (down, left) not in seen and rows[down][left] + 1 > 9:
            seen.append((down, left))
            flash(down, left)
        else:
            rows[down][left] += 1

    # south
    if down < n_rows:
        if (down, current_column) not in seen and rows[down][current_column] + 1 > 9:
            seen.append((down, current_column))
            flash(down, current_column)
        else:
            rows[down][current_column] += 1

    # south-east
    if down < n_rows and right < n_columns:
        if (down, right) not in seen and rows[down][right] + 1 > 9:
            seen.append((down, right))
            flash(down, right)
        else:
            rows[down][right] += 1


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    rows = [[int(n) for n in i.rstrip()] for i in input]
    n_rows = len(rows)
    n_columns = len(rows[0])

    step = 0
    while True:
        seen = list()
        for r, row in enumerate(rows):
            for c, energy_level in enumerate(row):
                rows[r][c] += 1
        for r, row in enumerate(rows):
            for c, energy_level in enumerate(row):
                if energy_level > 9 and (r, c) not in seen:
                    seen.append((r, c))
                    flash(r, c)
        for point in seen:
            rows[point[0]][point[1]] = 0
        if len(seen) == 100:
            print(step + 1)
        step += 1




