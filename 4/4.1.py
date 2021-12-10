import re


def check_bingo(boards):
    for i, board in enumerate(boards):
        for row in board['rows']:
            if all(row):
                return i+1
        for column in board['columns']:
            if all(column):
                return i+1
    return None


def compare_row_items_with_number(row_items, number, boards):
    for column, item in enumerate(row_items):
        if item == number:
            # print(f"board_number {board_number}, row: {row_normalized}, column: {column}")
            boards[board_number]['rows'][row_normalized][column] = 1
            boards[board_number]['columns'][column][row_normalized] = 1
            winner = check_bingo(boards)
            if winner:
                print(f"winner: {winner - 1}, number: {number}")
                return winner
    return None


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.readlines()

    extracted = input[0].split(',')

    number_of_boards = int(len(input[1:])/6)
    boards = []
    for i in range(number_of_boards):
        board = {
            'rows': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            'columns': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        }
        boards.append(board)

    winner = None
    final_number = None
    for number in extracted:
        if winner is None:
            board_number = 0
            for row, row_content in enumerate(input[2:]):
                row_normalized = row - 6 * board_number
                if row_content == '\n':
                    board_number += 1
                else:
                    row_items = row_content.rstrip().split()
                    winner = compare_row_items_with_number(row_items, number, boards)
                    final_number = number
                    if winner is not None:
                        break
        else:
            break

    start = (winner-1)*6 + 2    # skipping extracted line
    winning_board = input[start:start+5]
    print(f"winning_board: {winning_board}")
    print(final_number)

    sum_unmarked = 0
    for r, row in enumerate(boards[winner-1]['rows']):
        for c, row_element in enumerate(row):
            if row_element == 0:
                sum_unmarked += int(winning_board[r].split()[c])

    print(sum_unmarked)
    print(f"result {sum_unmarked * int(final_number)}")

# too high 62784











