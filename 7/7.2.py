import math
import statistics


def sum_n_numbers(n):
    return (n*(n+1))/2


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    positions = [int(x) for x in input[0].rstrip().split(',')]

    median = statistics.median(positions)
    mean = statistics.mean(positions)

    # the most optimized meeting point will be closer to the median
    if median < mean:
        meet = math.floor(mean)
    else:
        meet = math.ceil(mean)

    print(meet)
    distance = 0
    for p in positions:
        distance += sum_n_numbers(abs(p-meet))

    print(distance)

