import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    adj = [list(input())[:-1] for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    queue = deque([(0, 0)])

    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        cx, cy = queue.popleft()
        step = int(visited[cx][cy])

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < N
                and 0 <= ny < M
                and adj[nx][ny] != "0"
                and not visited[nx][ny]
            ):
                if nx == N - 1 and ny == M - 1:
                    print(step + 1)
                    return

                queue.append((nx, ny))
                visited[nx][ny] = step + 1


if __name__ == "__main__":
    main()
