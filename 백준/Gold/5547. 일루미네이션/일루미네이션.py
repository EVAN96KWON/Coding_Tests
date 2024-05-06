import sys
from collections import deque

input = sys.stdin.readline


def get_dirs(y):
    if y % 2:  # odd
        return ((0, 1), (1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1))
    else:  # even
        return ((0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))


def bfs(y, x):
    queue = deque([[y, x]])
    visited = [[False for _ in range(W + 2)] for _ in range(H + 2)]
    visited[y][x] = True

    cnt = 0
    while queue:
        y, x = queue.popleft()

        for dy, dx in get_dirs(y):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H + 2 and 0 <= nx < W + 2):
                continue

            if graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny, nx])
            elif graph[ny][nx] == 1:
                cnt += 1
    return cnt


if __name__ == "__main__":
    W, H = map(int, input().split())
    graph = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
    for i in range(1, H + 1):
        graph[i][1 : W + 1] = map(int, input().split())
    print(bfs(0, 0))
