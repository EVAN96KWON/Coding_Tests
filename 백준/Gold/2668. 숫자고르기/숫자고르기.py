import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(v, start):
    visited[v] = True

    w = graph[v]

    if not visited[w]:
        dfs(w, start)
    elif visited[w] and w == start:
        result.append(w)


if __name__ == "__main__":
    N = int(input())
    graph = {idx: int(input()) for idx in range(1, N + 1)}
    result = []

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(i, i)

    print(len(result))
    for res in sorted(result):
        print(res)
