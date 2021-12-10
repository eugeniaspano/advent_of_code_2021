
if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    initial_state = [int(x) for x in input[0].split(',')]
    counts = [0]*9
    reset_state = 6
    newborn = 8

    for fish_age in initial_state:
        counts[fish_age] += 1

    day = 0
    while day < 256:
        current_counts = counts.copy()
        for fish_age, fish_count_per_age in enumerate(current_counts):
            if fish_count_per_age > 0:
                if fish_age == 0:
                    counts[newborn] += fish_count_per_age
                    counts[reset_state] += fish_count_per_age
                    counts[fish_age] -= fish_count_per_age
                else:
                    counts[fish_age - 1] += fish_count_per_age
                    counts[fish_age] -= fish_count_per_age

        day += 1

    sum = 0
    for x in counts:
        sum += x

    print(sum)
