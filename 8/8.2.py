def is_list_complete(lista):
    for element in lista:
        if element == '':
            return False
    return True


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    final_solution = 0

    for line in input:
        number = ''
        numbers_to_decode = line.rstrip().split(' | ')[1].split()
        all_digits = line.rstrip().split(' | ')[0].split()
        encodings = [''] * 10

        all_digits.sort(key=len)

        encodings[1] = all_digits[0]
        encodings[7] = all_digits[1]
        encodings[4] = all_digits[2]
        encodings[8] = all_digits[-1]

        remaining_digits = [digit for digit in all_digits if digit not in encodings]
        encodings[3] = [digit for digit in remaining_digits if len(digit) == 5 and all(letter in digit for letter in encodings[1])][0]  # all letters of encoding[1] need to be in digit

        remaining_digits = [digit for digit in remaining_digits if digit not in encodings]
        encodings[9] = [digit for digit in remaining_digits if len(digit) == 6 and all(letter in digit for letter in encodings[3])][0]  # all letters of encoding[3] need to be in digit

        remaining_digits = [digit for digit in remaining_digits if digit not in encodings]
        encodings[0] = [digit for digit in remaining_digits if len(digit) == 6 and all(letter in digit for letter in encodings[1])][0]  # all letters of encoding[1] need to be in digit

        remaining_digits = [digit for digit in remaining_digits if digit not in encodings]
        encodings[6] = [digit for digit in remaining_digits if len(digit) == 6][0]

        remaining_digits = [digit for digit in remaining_digits if digit not in encodings]
        encodings[5] = [digit for digit in remaining_digits if len(digit) == 5 and all(letter in encodings[6] for letter in digit)][0]  # all letters of digit need to be in encoding[6]

        remaining_digits = [digit for digit in remaining_digits if digit not in encodings]
        encodings[2] = remaining_digits[0]

        for n in numbers_to_decode:
            for i, s in enumerate(encodings):
                if "".join(sorted(n)) == "".join(sorted(s)):
                    number += str(i)

        final_solution += int(number)

    print(final_solution)
