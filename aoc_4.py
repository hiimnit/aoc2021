input = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]

def parse_boards(file_name: str):
    boards = []
    with open(file_name, mode='r') as file:
        board = []
        for line in file:
            if line.strip() == '':
                boards.append(board)
                board = []
                continue

            board.append([int(e) for e in line.split(' ') if e.strip() != ''])

    return boards

def check_bingo(board: list[list[int or None]]) -> bool:
    for i in range(5):
        if all(e is None for e in board[i]):
            return True
        if all(board[j][i] is None for j in range(5)):
            return True
    return False

def mark_board(board: list[list[int or None]], n: int) -> bool:
    found = False
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == n:
                board[r][c] = None
                found = True
                break
        if found:
            break
    
    if found:
        return check_bingo(board)

    return False

def sum_board(board: list[list[int or None]]) -> int:
    total = 0
    for row in board:
        total += sum(e for e in row if e is not None)
    return total

if __name__ == '__main__':
    # part 1
    boards = parse_boards('aoc_4_boards.txt')

    found = False
    for n in input:
        for board in boards:
            bingo = mark_board(board, n)
            if bingo:
                print('result=', sum_board(board) * n)
                found = True
                break
        if found:
            break

    # part 2
    boards = parse_boards('aoc_4_boards.txt')
    solved = [False] * len(boards)

    result = None
    for n in input:
        for i, board in enumerate(boards):
            if not solved[i]:
                bingo = mark_board(board, n)
                if bingo:
                    result = sum_board(board) * n
                    solved[i] = True

        if all(solved):
            break

    print('result=', result)
