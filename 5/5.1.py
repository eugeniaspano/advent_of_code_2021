import collections
if __name__ == "__main__":
    file = open("input2.txt", "r")
    input = file.readlines()

    seen = []

    for line in input:
        start_end = line.split(" -> ")
        x1 = start_end[0].split(',')[0]
        y1 = start_end[0].split(',')[1]
        x2 = start_end[1].split(',')[0]
        y2 = start_end[1].split(',')[1].rstrip()

        if x1 == x2:
            if int(y1) > int(y2):
                higher = y1
                lower = y2
            else:
                higher = y2
                lower = y1
            for i in range(int(lower), int(higher)+1):
                point = (int(x1), i)
                seen.append(point)

        elif y1 == y2:
            if int(x1) > int(x2):
                higher = x1
                lower = x2
            else:
                higher = x2
                lower = x1
            for i in range(int(lower), int(higher)+1):
                point = (i, int(y1))
                seen.append(point)

    duplicates = [item for item, count in collections.Counter(seen).items() if count > 1]
    print(duplicates)
    print(len(duplicates))

