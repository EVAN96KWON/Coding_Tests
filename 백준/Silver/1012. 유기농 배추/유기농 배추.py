from collections import deque
from typing import List, Tuple


def init_map(
    M: int,
    N: int,
    K: int,
) -> Tuple[List[List[int]], List[List[bool]]]:
    baechoo = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        baechoo[y][x] = 1
    return baechoo, visited


def bfs(
    M: int,
    N: int,
    baechoo: List[List[int]],
    visited: List[List[bool]],
    queue: List[Tuple[int, int]],
) -> None:
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            cx, cy = x + dx, y + dy

            if (
                0 <= cx < M
                and 0 <= cy < N
                and not visited[cy][cx]
                and baechoo[cy][cx] == 1
            ):
                visited[cy][cx] = True
                queue.append((cx, cy))


def search(
    M: int,
    N: int,
    baechoo: List[List[int]],
    visited: List[List[bool]],
) -> int:
    cnt = 0
    for i in range(N):
        for j in range(M):
            if baechoo[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(M, N, baechoo, visited, deque([(j, i)]))
    return cnt


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = list(map(int, input().split()))
        baechoo, visited = init_map(M, N, K)
        print(search(M, N, baechoo, visited))
