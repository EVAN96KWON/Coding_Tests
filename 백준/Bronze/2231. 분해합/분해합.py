def get_smallest_constructor(num):
    for n in range(num):
        if N == n + sum(map(int, str(n))):
            return n
    return 0


if __name__ == "__main__":
    N = int(input())
    print(get_smallest_constructor(N))
