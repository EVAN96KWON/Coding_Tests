import bisect


def main():
    for t in range(int(input())):
        _list = sorted(list(map(int, input().split())))
        query = list(map(int, input().split()))
        answer = [len(_list) - bisect.bisect_right(_list, q) for q in query]
        print(*answer)


if __name__ == '__main__':
    main()

'''
4
3 5 1 7 9
1 0 6
1 3 5 7 9
1 3 5 7 9
-2 6 0 1 2 4
7 -4
7 6 5 4 3 2 1
0 1 2 3 4 5 6
'''