import sys
from collections import deque

input = sys.stdin.readline

MAX = 100001


def bfs(n, k):
    queue = deque()
    queue.append(n)
    visited = [0] * MAX
    res, cnt = 0, 0

    while queue:
        x = queue.popleft()
        if x == k:
            res = visited[x]
            cnt += 1
            continue

        for nx in (x - 1, x + 1, x * 2):
            if not 0 <= nx < MAX:
                continue

            if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return res, cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    res, cnt = bfs(n, k)
    print(res)
    print(cnt)
