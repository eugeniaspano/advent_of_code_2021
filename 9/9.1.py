if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    lines = [list(i.rstrip()) for i in input]
    n_rows = len(lines)
    n_columns = len(lines[0])

    solution = 0

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
            solution += int(cell_value) + 1

    print(solution)
