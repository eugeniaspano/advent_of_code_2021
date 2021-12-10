if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    number = 0
    for i, line in enumerate(lines):
        if i < len(lines)-3:
            if (int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])) - (int(lines[i]) + int(lines[i+1]) + int(lines[i+2])) > 0:
                number += 1

    print(number)

