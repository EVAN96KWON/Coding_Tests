import bisect


def main():
    for TC in range(int(input())):
        arr = sorted(list(map(int, input().split())))
        find = list(map(int, input().split()))
        count = 0
        for f in find:
            count += bisect.bisect_right(arr, f) - bisect.bisect_left(arr, f)
        print(count)


if __name__ == '__main__':
    main()
