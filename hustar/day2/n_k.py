def power(n, k, m):
    if k == 0:
        return 1
    if k == 1:
        return n

    half = power(n, k // 2, m)

    if k % 2 == 0:
        return (half * half) % m
    else:
        return (half * half * n) % m


def main():
    for TC in range(int(input())):
        n, k, m = map(int, input().split())
        print(power(n, k, m))


if __name__ == '__main__':
    main()
