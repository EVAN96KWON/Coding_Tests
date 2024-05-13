import sys

input = sys.stdin.readline
dp = [0, 0, 1]


def fibonacci(N: int):
    global dp

    while len(dp) < N + 2:
        dp.append(dp[-1] + dp[-2])

    return dp[N + 1]


if __name__ == "__main__":
    N = int(input())
    print(fibonacci(N))
