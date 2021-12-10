
def explore(input_lines, row_number, column_number, seen):
    up = row_number-1
    right = column_number+1
    down = row_number+1
    left = column_number-1

    if right < n_columns:
        if int(input_lines[row_number][right]) > int(input_lines[row_number][column_number]) and \
                int(input_lines[row_number][right]) != 9 and (row_number, right) not in seen:
            seen.append((row_number, right))
            explore(input_lines, row_number, right, seen)

    if up >= 0:
        if int(input_lines[up][column_number]) > int(input_lines[row_number][column_number]) and \
                int(input_lines[up][column_number]) != 9 and (up, column_number) not in seen:
            seen.append((up, column_number))
            explore(input_lines, up, column_number, seen)

    if left >= 0:
        if int(input_lines[row_number][left]) > int(input_lines[row_number][column_number]) and \
                int(input_lines[row_number][left]) != 9 and (row_number, left) not in seen:
            seen.append((row_number, left))
            explore(input_lines, row_number, left, seen)

    if down < n_rows:
        if int(input_lines[down][column_number]) > int(input_lines[row_number][column_number]) and \
                int(input_lines[down][column_number]) != 9 and (down, column_number) not in seen:
            seen.append((down, column_number))
            explore(input_lines, down, column_number, seen)

    return seen


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    lines = [list(i.rstrip()) for i in input]
    n_rows = len(lines)
    n_columns = len(lines[0])

    low_points = []

    for r, row in enumerate(lines):
        for c, cell_value in enumerate(row):
            if c+1 < n_columns:
                if row[c+1] <= cell_value:
                    continue
            if c-1 >= 0:
                if row[c-1] <= cell_value:
                    continue
            if r+1 < n_rows:
                if lines[r+1][c] <= cell_value:
                    continue
            if r-1 >= 0:
                if lines[r-1][c] <= cell_value:
                    continue
            low_points.append((r, c))

    basins = []
    for low_point in low_points:
        basin_size = len(explore(lines, low_point[0], low_point[1], [])) + 1
        basins.append(basin_size)

    sorted_b = sorted(basins)
    solution = sorted_b[-1]*sorted_b[-2]*sorted_b[-3]
    print(solution)



