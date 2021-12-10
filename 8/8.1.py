if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    digit_frequency = [0] * 10
    ones_sevens_fours_eights = 0

    for line in input:
        digits = line.rstrip().split(' | ')[1].split()
        for digit in digits:
            number_of_segments = len(digit)
            if number_of_segments == 2:
                digit_frequency[1] += 1
                ones_sevens_fours_eights += 1
            elif number_of_segments == 3:
                digit_frequency[7] += 1
                ones_sevens_fours_eights += 1
            elif number_of_segments == 4:
                digit_frequency[4] += 1
                ones_sevens_fours_eights += 1
            elif number_of_segments == 7:
                digit_frequency[8] += 1
                ones_sevens_fours_eights += 1

    print(ones_sevens_fours_eights)

