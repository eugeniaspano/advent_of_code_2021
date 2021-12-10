import math

if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    scores = []
    for i, line in enumerate(input):
        found_open = []
        e = 0
        for character in list(line.rstrip()):
            if character in parentheses:
                found_open.append(character)
            else:
                expected_character = parentheses[found_open[-1]]
                if character == expected_character:
                    found_open = found_open[:-1]
                else:
                    e = 1
                    break
        if e != 1:
            characters_to_complete = [parentheses[c] for c in found_open]
            characters_to_complete.reverse()
            score = 0
            for c in characters_to_complete:
                score = 5*score + points[c]

            scores.append(score)

    sorted_scores = sorted(scores)
    solution = sorted_scores[math.floor(len(scores)/2)]

    print(solution)
