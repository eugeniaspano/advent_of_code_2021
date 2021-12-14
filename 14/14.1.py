from collections import defaultdict

if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    # note to self: this could have been achieved with just one dictionary and using two letters as key
    adjacent_letters_template = defaultdict(lambda: defaultdict(int))
    adjacent_letters_next = defaultdict(lambda: defaultdict(int))

    template = input[0].rstrip()

    for i, letter in enumerate(template):
        if i < len(template) - 1:
            adjacent_letters_template[letter][template[i + 1]] += 1

    for step in range(10):

        adjacent_letters_next = defaultdict(lambda: defaultdict(int))

        for line in input[2:]:
            pair = line.rstrip().split(' -> ')[0]
            new_letter = line.rstrip().split(' -> ')[1]

            if pair[1] in adjacent_letters_template[pair[0]]:
                adjacent_letters_next[pair[0]][new_letter] += adjacent_letters_template[pair[0]][pair[1]]
                adjacent_letters_next[new_letter][pair[1]] += adjacent_letters_template[pair[0]][pair[1]]

        adjacent_letters_template = adjacent_letters_next

    count_of_letters = defaultdict(int)
    for letter in adjacent_letters_next:
        for other_letter in adjacent_letters_next[letter]:
            count_of_letters[other_letter] += adjacent_letters_next[letter][other_letter]

    # accounting for the first letter of the template which would otherwise be skipped
    count_of_letters[input[2][0]] += 1

    print(count_of_letters)
    print(max(count_of_letters.values())-min(count_of_letters.values()))








