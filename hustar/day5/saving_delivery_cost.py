def main():
    for t in range(int(input())):
        n, C = map(int, input().split())
        w = list(map(int, input().split()))
        v = list(map(int, input().split()))
        T = [[0] * (C + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, C + 1):
                if i == 0:
                    if w[i] > j:
                        T[i][j] = 0
                    else:
                        T[i][j] = v[i]
                else:
                    if w[i] > j:
                        T[i][j] = T[i - 1][j]
                    else:
                        T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i]] + v[i])
        print(T[n - 1][C])


if __name__ == '__main__':
    main()

'''
3
1 5
3
100
5 10
2 1 1 4 4
34 686 668 678 560
10 10
3 2 5 4 1 3 1 2 5 5
702 130 533 375 819 902 203 660 305 581
'''