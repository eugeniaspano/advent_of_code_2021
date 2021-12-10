import copy
from collections import OrderedDict


def check_bingo(boards, winners):
    for i, board in enumerate(boards):
        for row in board['rows']:
            if all(row):
                if i not in winners:
                    return i
        for column in board['columns']:
            if all(column):
                if i not in winners:
                    return i
    return None


def mark_number_in_row(row_content, number, boards, board_number, row):
    row_items = row_content.rstrip().split()
    for column, item in enumerate(row_items):
        if item == number:
            boards[board_number]['rows'][row][column] = 1
            boards[board_number]['columns'][column][row] = 1
    return boards


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def main():
    file = open("input.txt", "r")
    input = file.readlines()

    extracted = input[0].split(',')

    number_of_boards = int(len(input[1:]) / 6)
    boards = []
    for i in range(number_of_boards):
        board = {
            'rows': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            'columns': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        }
        boards.append(board)

    winners = OrderedDict()
    for number in extracted:
        board_number = 0
        for row, row_content in enumerate(input[2:]):
            row_normalized = row - 6 * board_number     # 6 = one board + one empty line
            if row_content == '\n':
                board_number += 1
            else:
                boards = mark_number_in_row(row_content, number, boards, board_number, row_normalized)
                new_winner = check_bingo(boards, winners)
                final_number = number
                if new_winner is not None:
                    if new_winner not in winners:
                        winners[new_winner] = (final_number, copy.deepcopy(boards[new_winner]))

    winners_unique = unique(winners.keys())
    last_winner = winners_unique[-1]

    winning_number = winners[last_winner][0]

    start = last_winner * 6 + 2  # skipping extracted line and first empty line
    winning_board = input[start:start + 5]  # 5 is the length of one board

    sum_unmarked = 0
    for r, row in enumerate(winners[last_winner][1]['rows']):
        for c, row_element in enumerate(row):
            if row_element == 0:
                sum_unmarked += int(winning_board[r].split()[c])    # .split since winning_board[r] is a string

    print(f"result {sum_unmarked * int(winning_number)}")


if __name__ == "__main__":
    main()











