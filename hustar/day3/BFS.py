from collections import deque


def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


def main():
    for TC in range(int(input())):
        N, M = map(int, input().split())
        graph = {_: [] for _ in range(N)}

        for m in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)

        for g in graph.values():
            g.sort()

        print(*bfs(graph, 0))


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