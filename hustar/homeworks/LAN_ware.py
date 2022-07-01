from collections import deque


def infect(graph, root):
    infected = [False] * len(graph.keys())
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if not infected[node]:
            infected[node] = True
            queue.extend(graph[node])
    return infected.count(True)


def main():
    for T in range(int(input())):
        N, M, K = map(int, input().split())
        graph = {_: [] for _ in range(N)}

        for m in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        print(N - infect(graph, K))


if __name__ == '__main__':
    main()

'''
4
2 1 0
0 1
5 4 2
2 4
3 2
3 1
0 4
7 9 6
0 1
0 2
4 5
0 4
0 5
2 4
1 4
1 5
6 3
10 12 5
1 5
8 1
8 6
4 8
9 7
4 6
1 3
3 7
5 6
9 8
5 9
7 4
'''