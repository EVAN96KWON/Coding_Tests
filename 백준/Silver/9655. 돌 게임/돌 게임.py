import sys

input = sys.stdin.readline

dp = [None, True, False, True]


def stone_game(n):
    global dp

    if len(dp) > n:
        return dp[n]

    for i in range(4, n + 1):
        if dp[i - 1] or dp[i - 3]:
            dp[i] = False
        else:
            dp[i] = True

    return dp[n]


if __name__ == "__main__":
    N = int(input())
    print("SK" if N % 2 else "CY")
