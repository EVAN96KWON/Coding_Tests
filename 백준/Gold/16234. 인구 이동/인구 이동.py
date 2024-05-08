from collections import deque
import sys

input = sys.stdin.readline


def bfs(r, c, visited):
    queue = deque([(r, c)])
    union = set([(r, c)])

    while queue:
        r, c = queue.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc

            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                continue

            if L <= abs(A[r][c] - A[nr][nc]) <= R:
                visited[nr][nc] = True
                queue.append((nr, nc))
                union.add((nr, nc))

    if len(union) < 2:
        return 0

    avg = sum(A[r][c] for r, c in union) // len(union)
    for r, c in union:
        A[r][c] = avg

    return 1


def move():
    for day in range(2001):
        can_move = 0
        visited = [[False] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    visited[r][c] = True
                    can_move += bfs(r, c, visited)

        if not can_move:
            return day


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(move())
