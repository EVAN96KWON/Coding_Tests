def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == "__main__":
    graph = {n + 1: [] for n in range(int(input()))}
    for _ in range(int(input())):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (len(graph) + 1)
    dfs(graph, 1, visited)
    print(sum(visited[1:]) - 1)
