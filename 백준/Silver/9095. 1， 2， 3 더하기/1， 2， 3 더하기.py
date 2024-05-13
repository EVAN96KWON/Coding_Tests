import sys

input = sys.stdin.readline

dp = [1, 2, 4]


def answer(n):
    while len(dp) < n + 1:
        dp.append(sum(dp[-3:]))
    return dp[n - 1]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(answer(n))
