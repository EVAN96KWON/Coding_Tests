def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    return max([n for row in board for n in row]) ** 2


if __name__ == '__main__':
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
