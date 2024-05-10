from collections import deque
import sys

input = sys.stdin.readline


def bfs(I, start, end):
    board = [[0] * I for _ in range(I)]
    dirs = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))

    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return board[y][x]

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < I and 0 <= ny < I):
                continue

            if board[ny][nx]:
                continue

            queue.append((nx, ny))
            board[ny][nx] = board[y][x] + 1

    return -1


if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        I = int(input())
        start = tuple(map(int, input().split()))
        end = tuple(map(int, input().split()))
        print(bfs(I, start, end))
