import sys

input = sys.stdin.readline

dp = [0, 1, 2]


def tiling(N):
    while len(dp) <= N:
        dp.append((dp[-1] + dp[-2]) % 10007)

    return dp[N]


if __name__ == "__main__":
    N = int(input())
    print(tiling(N))
