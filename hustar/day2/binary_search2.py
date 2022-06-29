import bisect


def main():
    for TC in range(int(input())):
        arr = list(map(int, input().split()))
        find = list(map(int, input().split()))
        answer = list()

        print(arr)
        print(find)

        for f in find:
            cache = []
            upper = bisect.bisect(arr, f)
            lower = upper - 1

            if upper in range(len(arr)):
                cache.append((arr[upper], f - arr[upper]))

            if lower in range(len(arr)):
                cache.append((arr[lower], f - arr[lower]))

            cache.sort(key=lambda x: (abs(x[1]), x[0]))
            print(cache)

            answer.append(cache[0][0])

        print(*answer)


if __name__ == '__main__':
    main()

'''
3
2 4 6 8 10
1 3 7
1 3 5 7
2 3 6
3 7 11 17 21
9 8 4 100 16 17
'''
'''
1
3 7 11 17 21
9 8 4 100 16 17
'''
