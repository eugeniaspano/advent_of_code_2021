import statistics
import sys

if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    positions = [int(x) for x in input[0].rstrip().split(',')]

    m = statistics.median(positions)

    distance = 0
    for p in positions:
        distance += abs(p-m)

    print(distance)

    # 333 too low
    # 464
