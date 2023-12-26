primes = []


def init_primes(n):
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False


if __name__ == '__main__':
    M, N = map(int, input().split())
    if not primes:
        init_primes(1000000)

    for p in primes:
        if M <= p <= N:
            print(p)
        elif N < p:
            break
