
def explore(current_cave, small_caves_seen, path, seen_twice):
    global n_paths
    global paths

    path.append(current_cave)

    if current_cave == 'end':
        paths.append(path.copy())
        n_paths += 1
        return

    if current_cave.islower() and current_cave != 'start':
        if current_cave not in small_caves_seen:
            small_caves_seen.add(current_cave)
        else:
            if len(seen_twice) == 0:
                seen_twice.add(current_cave)
            else:
                return

    for cave in connections[current_cave]:
        explore(cave, small_caves_seen.copy(), path.copy(), seen_twice.copy())


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    connections = dict()
    for line in input:
        parts = line.rstrip().split('-')
        if parts[0] not in connections:
            if parts[1] != 'start' and parts[0] != 'end':
                connections[parts[0]] = [parts[1]]
        else:
            if parts[1] != 'start' and parts[0] != 'end':
                connections[parts[0]].append(parts[1])

        if parts[1] not in connections:
            if parts[0] != 'start' and parts[1] != 'end':
                connections[parts[1]] = [parts[0]]
        else:
            if parts[0] != 'start' and parts[1] != 'end':
                connections[parts[1]].append(parts[0])

    n_paths = 0
    paths = []

    for cave in connections['start']:
        path = ['start']
        small_caves_seen = {'start'}
        seen_twice = set()

        explore(cave, small_caves_seen, path, seen_twice)

    print(n_paths)
