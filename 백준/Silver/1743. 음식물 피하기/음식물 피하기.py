from collections import deque


def bfs(graph, start, visited):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([start])
    visited.add(start)
    size = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny]
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))
                size += 1

    return size


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    graph = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split())
        graph[r - 1][c - 1] = True

    max_size = 0
    visited = set()

    for i in range(N):
        for j in range(M):
            if graph[i][j] and (i, j) not in visited:
                max_size = max(max_size, bfs(graph, (i, j), visited))

    print(max_size)
