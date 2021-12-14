if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    fold_instructions = [x.rstrip() for x in input if x.startswith('fold along')]

    (fold_instruction_axis, fold_instruction_value) = fold_instructions[0].split()[2].split('=')
    print(fold_instruction_axis, fold_instruction_value)

    points = set()
    for line in input:
        if line.rstrip() == '':
            break
        y_value = int(line.rstrip().split(',')[1])
        x_value = int(line.rstrip().split(',')[0])
        if fold_instruction_axis == 'y':
            if y_value >= int(fold_instruction_value):
                y_value -= 2*(y_value - int(fold_instruction_value))
        if fold_instruction_axis == 'x':
            if x_value >= int(fold_instruction_value):
                x_value -= 2*(x_value - int(fold_instruction_value))

        points.add((x_value, y_value))

    print(len(points))


