from collections import deque


def dfs(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited


def main():
    for TC in range(int(input())):
        N, M = map(int, input().split())
        graph = {_: [] for _ in range(N)}

        for m in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        for g in graph.values():
            g.sort()

        print(*dfs(graph, 0))


if __name__ == '__main__':
    main()

'''
3
4 4
0 1
0 3
1 2
1 3
5 7
0 1
0 2
0 4
1 3
1 4
2 4
3 4
6 5
0 5
5 4
1 4
1 3
2 3
'''