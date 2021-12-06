from pprint import pprint


def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def parse_input(input_data):
    numbers = [int(x) for x in input_data[0].split(',')]
    boards = []

    curr_board = []
    for row in input_data[2:]:
        if not row:
            boards.append(curr_board)
            curr_board = []
        else:
            curr_board.append([int(x) for x in row.split()])
    boards.append(curr_board)

    return boards, numbers 


def _calculate_score_if_winning(board, i, j):
    row = board[i]
    column = [board[x][j] for x in range(len(board))]
    is_winning = all([x < 0 for x in row])
    is_winning = is_winning or all([x < 0 for x in column])

    if not is_winning:
        return None

    total_sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            total_sum += max(board[i][j], 0)
    return total_sum


def _mark_board(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                # use negative numbers as markers
                board[i][j] = -number
                return board, _calculate_score_if_winning(board, i, j)
    
    return board, None


def solve_part_one(boards, numbers):
    for number in numbers:
        for board in boards:
            board, board_score = _mark_board(board, number)
            if board_score is not None:
                return board_score * number 


def solve_part_two(boards, numbers):
    for number in numbers:
        next_boards = []
        last_total_board_score = None
        for board in boards:
            board, board_score = _mark_board(board, number)
            if board_score is None:
                next_boards.append(board)
            else:
                last_total_board_score = board_score * number
        boards = next_boards

        if not boards:
            return last_total_board_score


if __name__ == "__main__":
    input_data = read_input("input.txt")
    boards, numbers = parse_input(input_data)
    #pprint(boards)
    #print(numbers)

    print(solve_part_one(boards, numbers))
    print(solve_part_two(boards, numbers))
