def init_primes():
    n = 100000
    a = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False

    return [_ for _ in range(2, n) if a[_]]


def init_under_prime():
    n = 100001
    a = [0] * n

    for p in primes:
        for i in range(p, len(a), p):
            idx = i
            while idx % p == 0:
                a[i] += 1
                idx = int(idx / p)

    return a


primes = init_primes()
under_primes = init_under_prime()


if __name__ == '__main__':
    A, B = map(int, input().split())
    cnt = 0

    for i in range(A, B + 1):
        if under_primes[i] in primes:
            cnt += 1

    print(cnt)
    #1124
