def board_reset(m, n, board):
    movable = True

    while movable:
        movable = False
        for y in range(m - 1):
            for x in range(n):
                if board[y][x] != '0' and board[y + 1][x] == '0':
                    movable = True
                    board[y + 1][x] = board[y][x]
                    board[y][x] = '0'

    return board


def check_pop(m, n, board):
    deleted_cnt = 0
    tmp = [[False for _ in range(n)] for __ in range(n)]

    # check 2x2
    for y in range(m - 1):
        for x in range(n - 1):
            if board[y][x] == '0':
                continue
            if board[y][x] != board[y + 1][x]:
                continue
            if board[y][x] != board[y][x + 1]:
                continue
            if board[y][x] != board[y + 1][x + 1]:
                continue
            tmp[y][x] = tmp[y + 1][x] = tmp[y][x + 1] = tmp[y + 1][x + 1] = True

    # delete
    for y in range(m):
        for x in range(n):
            if tmp[y][x]:
                deleted_cnt += 1
                board[y][x] = '0'

    board = board_reset(m, n, board)

    return board, deleted_cnt


def solution(m, n, board):
    answer = 0
    pop_cnt = 0

    for y in range(m):
        board[y] = list(board[y])

    board, pop_cnt = check_pop(m, n, board)
    answer += pop_cnt

    while pop_cnt != 0:
        board, pop_cnt = check_pop(m, n, board)
        answer += pop_cnt

    return answer


if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
