if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    freq = []

    positions = len(input[0].rstrip())

    list_of_oxygen = list(set(input.copy()))
    list_of_co2 = list(set(input.copy()))

    for i in range(positions):
        freq = [0, 0]
        for n in list_of_oxygen:
            freq[int(n[i])] += 1

        if freq[0] > freq[1]:
            list_of_oxygen = [number for number in list_of_oxygen if number[i] == '0']
        else:
            list_of_oxygen = [number for number in list_of_oxygen if number[i] == '1']
        if len(list_of_oxygen) == 1:
            break

    for i in range(positions):
        freq = [0, 0]
        for n in list_of_co2:
            freq[int(n[i])] += 1

        if freq[0] > freq[1]:
            list_of_co2 = [number for number in list_of_co2 if number[i] == '1']
        else:
            list_of_co2 = [number for number in list_of_co2 if number[i] == '0']
        if len(list_of_co2) == 1:
            break

    print(f"list_of_numbers: {list_of_oxygen}")
    print(f"co2: {list_of_co2}")

    print(f"result: {int(list_of_co2[0].rstrip(), 2) * int(list_of_oxygen[0].rstrip(), 2)}")










