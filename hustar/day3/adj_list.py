def main():
    for TC in range(int(input())):
        N, M = map(int, input().split())
        graph = {_: [] for _ in range(N)}

        for m in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        for g in graph.values():
            print(*sorted(g))


if __name__ == '__main__':
    main()

'''
2
4 4
0 1
0 3
1 2
1 3
5 6
0 1
0 3
0 4
3 4
1 4
1 3
'''