def max_sub_seq(arr):
    cache = [arr[0]] + [None] * (len(arr) - 1)

    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)


def main():
    for TC in range(int(input())):
        print(max_sub_seq(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
