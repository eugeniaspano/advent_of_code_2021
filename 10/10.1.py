if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    parentheses = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    open_parentheses = ['(', '[', '{', '<']
    closed_parentheses = [')', ']', '}', '>']

    errors = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    for line in input:
        found_open = []
        for character in list(line.rstrip()):
            if character in parentheses:
                found_open.append(character)
            else:
                expected_character = parentheses[found_open[-1]]
                if character == expected_character:
                    found_open = found_open[:-1]
                else:
                    errors[character] += 1

                    break

    print(errors)

    solution = errors[')']*3 + errors[']']*57 + errors['}']*1197 + errors['>']*25137

    print(solution)