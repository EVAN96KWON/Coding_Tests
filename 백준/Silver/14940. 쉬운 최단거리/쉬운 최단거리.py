import sys
from collections import deque

input = sys.stdin.readline


def init_mat(n, m):
    mat = []
    start = (-1, -1)
    walls = set()
    for y in range(n):
        row = input().split()
        for x in range(m):
            curr = row[x]
            if curr == "2":
                start = (x, y)
            elif curr == "0":
                walls.add((x, y))
        mat.append(row)
    return mat, start, walls


def bfs(mat, visited, queue):
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < m
                and 0 <= ny < n
                and mat[ny][nx] == "1"
                and visited[ny][nx] == -1
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat, start, walls = init_mat(n, m)
    queue = deque([start])
    visited = [[-1] * m for _ in range(n)]
    visited[start[1]][start[0]] = 0
    bfs(mat, visited, queue)
    for wx, wy in walls:
        visited[wy][wx] = 0
    for row in visited:
        print(*row)
