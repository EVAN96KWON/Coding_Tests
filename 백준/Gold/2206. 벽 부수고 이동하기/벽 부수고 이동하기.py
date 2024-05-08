from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][y][x] = 1
    visited[1][y][x] = 1
    queue = deque([(x, y, 0)])
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        x, y, z = queue.popleft()

        if x == M - 1 and y == N - 1:
            return visited[1][y][x]

        for dx, dy in dirs:
            nx, ny, nz = x + dx, y + dy, z

            if not (0 <= nx < M and 0 <= ny < N):
                continue

            if visited[nz][ny][nx] > 0 or board[ny][nx] == "1":
                continue

            visited[nz][ny][nx] = visited[z][y][x] + 1
            queue.append((nx, ny, nz))

        if not z:
            for dx, dy in dirs:
                nx, ny, nz = x + dx, y + dy, z + 1

                if not (0 <= nx < M and 0 <= ny < N):
                    continue

                if visited[nz][ny][nx] > 0:
                    continue

                visited[nz][ny][nx] = visited[z][y][x] + 1
                queue.append((nx, ny, nz))

    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input())[:-1] for _ in range(N)]
    print(bfs(0, 0))
