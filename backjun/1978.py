def init_primes():
    n = 1000
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]


primes = [] * 1001

if __name__ == '__main__':
    N = int(input())
    n_list = list(map(int, input().split()))
    primes = init_primes()
    print(len([_ for _ in n_list if _ in primes]))
