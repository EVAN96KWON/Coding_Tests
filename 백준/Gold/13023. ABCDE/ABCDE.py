import sys

input = sys.stdin.readline


def dfs(idx, depth=0):
    global ret
    visited[idx] = True
    if depth == 4:
        ret = True
        return

    for i in graph[idx]:
        if visited[i]:
            continue

        visited[i] = True
        dfs(i, depth + 1)
        visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    visited = [False] * (N + 1)
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    ret = False
    for i in range(N):
        dfs(i)
        visited[i] = False
        if ret:
            break
    print(int(ret))
