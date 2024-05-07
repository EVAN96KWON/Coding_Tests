from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    queue = deque([[0, 0, 0]])
    visited[0][0][0] = 1

    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    horse = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]

    while queue:
        x, y, z = queue.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][z] - 1

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < H and 0 <= ny < W):
                continue

            if visited[nx][ny][z] or board[nx][ny]:
                continue

            visited[nx][ny][z] = visited[x][y][z] + 1
            queue.append([nx, ny, z])

        if z < K:
            for dx, dy in horse:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < H and 0 <= ny < W):
                    continue

                if visited[nx][ny][z + 1] or board[nx][ny]:
                    continue

                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                queue.append([nx, ny, z + 1])

    return -1


if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    print(bfs())
