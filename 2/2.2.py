if __name__ == "__main__":
    file = open("2.txt")
    lines = file.readlines()

    forward = 0
    depth = 0
    aim = 0

    for line in lines:
        if line.split(' ')[0] == "forward":
            forward = forward + int(line.split(' ')[1])
            depth = depth + int(line.split(' ')[1])*aim
        elif line.split(' ')[0] == "down":
            aim = aim + int(line.split(' ')[1])
        elif line.split(' ')[0] == "up":
            aim = aim - int(line.split(' ')[1])

    print(forward * depth)
