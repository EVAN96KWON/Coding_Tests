import sys

input = sys.stdin.readline

dp = [0, 1, 3]


def tiling(N):
    while len(dp) <= N:
        dp.append(dp[-1] + 2 * dp[-2])

    return dp[N] % 10007


if __name__ == "__main__":
    N = int(input())
    print(tiling(N))
