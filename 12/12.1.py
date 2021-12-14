import collections


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


def explore(current_cave, small_caves_seen, path):
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
            return

    for cave in connections[current_cave]:
        explore(cave, small_caves_seen.copy(), path.copy())


if __name__ == "__main__":
    file = open("input2.txt", "r")
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

    # removing dead paths
    for c in connections:
        if len(connections[c]) == 1 and connections[c][0].islower():
            connections = removekey(connections, c)

            for c2 in connections:
                if c in connections[c2]:
                    connections[c2] = [x for x in connections[c2] if x != c]

    print(connections)

    n_paths = 0
    paths = []

    for cave in connections['start']:
        path = ['start']
        small_caves_seen = {'start'}

        explore(cave, small_caves_seen, path)

    print(paths)
    print(n_paths)
