if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    freq = []

    positions = len(input[0].rstrip())
    frequency_per_position = [[0, 0] for i in range(positions)]

    for line in input:
        for i, number in enumerate(line.rstrip()):
            frequency_per_position[i][int(number)] += 1

    print(frequency_per_position)

    gamma = ''
    epsilon = ''

    for freq in frequency_per_position:
        if freq[0] > freq[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2) * int(epsilon, 2))
