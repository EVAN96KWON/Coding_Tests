def main():
    max_num = 1000000
    dp = [1 for _ in range(max_num + 1)]
    dp[2] = 2
    dp[3] = 4
    for i in range(4, max_num+1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1904101441

    for t in range(int(input())):
        print(dp[int(input())])


if __name__ == '__main__':
    main()

'''
7
1
2
3
4
5
10
100
'''