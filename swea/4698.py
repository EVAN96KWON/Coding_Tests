def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] is True]


primes = prime_list(1000000)

T = int(input())

for test_case in range(1, T + 1):
    D, A, B = map(int, input().split())
    cnt = 0

    for prime in primes:
        cnt += 1 if A <= prime <= B and str(D) in str(prime) else 0

    print(f'#{test_case} {cnt}')
