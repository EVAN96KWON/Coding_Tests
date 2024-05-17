import sys

input = sys.stdin.readline

def init():
    global dp
    
    for n in range(2, N + 1):
        for last in range(10):
            if last == 0:
                dp[n][last] = dp[n - 1][1]
            elif last == 9:
                dp[n][last] = dp[n - 1][8]
            else:
                dp[n][last] = dp[n - 1][last - 1] + dp[n - 1][last + 1]
    

if __name__ == "__main__":
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    init()
    print(sum(dp[N]) % 1000000000)
