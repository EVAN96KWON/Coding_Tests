import sys
from collections import deque


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs():
    while queue:
        curr = queue.popleft()
        for child in graph[curr]:
            if parents[child] == 0:
                parents[child] = curr
                queue.append(child)


def init_graph(N):
    graph = {n + 1: [] for n in range(N)}
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


if __name__ == "__main__":
    N = int(input())
    graph = init_graph(N)
    queue = deque([1])
    parents = [0] * (N + 1)
    bfs()
    print("\n".join(map(str, parents[2:])))
