def solution(n, money):
    combs = [1] + [0] * n

    for coin in money:
        for i in range(coin, n + 1):
            combs[i] += combs[i - coin]

    return combs[-1]
