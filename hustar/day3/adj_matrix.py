def main():
    for TC in range(int(input())):
        N, M = map(int, input().split())
        mat = [[0 for _ in range(N)] for __ in range(N)]

        for m in range(M):
            u, v, c = map(int, input().split())
            mat[u][v] = c

        for row in mat:
            print(*row)


if __name__ == '__main__':
    main()

'''
2
4 6
0 1 3
0 3 7
1 2 2
1 3 5
2 0 3
3 2 3
5 10
0 1 1
0 2 1
0 4 1
1 0 1
1 3 2
1 4 1
2 4 1
3 4 1
4 1 1
4 2 2
'''