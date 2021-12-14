if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    fold_instructions = [x.rstrip() for x in input if x.startswith('fold along')]

    (fold_instruction_axis, fold_instruction_value) = fold_instructions[0].split()[2].split('=')
    print(fold_instruction_axis, fold_instruction_value)

    my_points = set()
    for line in input:
        if line.rstrip() == '':
            break
        y_value = int(line.rstrip().split(',')[1])
        x_value = int(line.rstrip().split(',')[0])
        my_points.add((x_value, y_value))

    points = set()
    for instructions in fold_instructions:
        points = set()
        (fold_instruction_axis, fold_instruction_value) = instructions.split()[2].split('=')
        for point in my_points:
            x_value = point[0]
            y_value = point[1]
            if fold_instruction_axis == 'y':
                if y_value >= int(fold_instruction_value):
                    y_value -= 2*(y_value - int(fold_instruction_value))
            if fold_instruction_axis == 'x':
                if x_value >= int(fold_instruction_value):
                    x_value -= 2*(x_value - int(fold_instruction_value))

            points.add((x_value, y_value))
        my_points = points

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    # representation = [['.'] * (max_x + 1)].copy() * (max_y + 1) <--- did not work
    representation = []
    for y in range(max_y+1):
        representation.append(['.'] * (max_x + 1))

    for point in points:
        representation[point[1]][point[0]] = '@'
    for row in representation:
        print(row)

