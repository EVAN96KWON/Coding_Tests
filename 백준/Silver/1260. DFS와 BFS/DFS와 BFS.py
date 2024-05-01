import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue += sorted(graph[v])
    return visited


def dfs(graph, start):
    visited = []
    stack = deque([start])
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack += sorted(graph[v], reverse=True)
    return visited


if __name__ == "__main__":
    N, M, V = list(map(int, input().split()))
    graph = {n: [] for n in range(1, N + 1)}
    for _ in range(M):
        s, e = list(map(int, input().split()))
        graph[s].append(e)
        graph[e].append(s)
    print(*dfs(graph, V))
    print(*bfs(graph, V))