if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    state = [int(x) for x in input[0].split(',')]

    reset_state = 6
    newborn = 8

    day = 0
    while day < 80:
        newborns = 0
        for i, s in enumerate(state):
            if s == 0:
                state[i] = reset_state
                newborns += 1
            else:
                state[i] -= 1
        state.extend([newborn]*newborns)
        day += 1

    print(f"Solution: {len(state)}")





