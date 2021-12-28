def get_version(string):
    return int("".join([x for x in string[:3]]), base=2)


def get_type(string):
    return int("".join([x for x in string[3:6]]), base=2)


def parse_literal_number(string):
    first_bit = 1
    number = ''
    i = 0
    while first_bit != 0:
        first_bit = int(string[i])
        number += string[i + 1:i + 5]
        i += 5
    print(f"number: {int(number, 2)}")
    return string[i:]


def parse_packet(string):
    global versions

    version = get_version(string)
    type = get_type(string)
    versions += version

    if type == 4:
        return parse_literal_number(string[6:])
    else:
        length_type_id = string[6]
        if length_type_id == '0':
            length_sub_packages = int(string[7:22], base=2)
            subpackages = string[22:22 + length_sub_packages]
            while len(subpackages) > 0:
                subpackages = parse_packet(subpackages)
            return string[22+length_sub_packages:]

        else:
            n_subpackages = int(string[7:18], base=2)
            string = string[18:]
            for n in range(n_subpackages):
                string = parse_packet(string)
            return string


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    # input = ['A0016C880162017C3686B18A3D4780']
    versions = 0

    length = 4*len(input[0])
    thingy = '0' + str(length) + 'b'

    base10_string = int(input[0], base=16)
    base2_string = format(base10_string, thingy)

    parse_packet(base2_string)

    print(versions)











