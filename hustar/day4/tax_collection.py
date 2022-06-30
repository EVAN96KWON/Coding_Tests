def main():
    coins = (50000, 10000, 5000, 1000, 500, 100)
    for T in range(int(input())):
        tax = int(input())
        answer = 0
        for coin in coins:
            if tax // coin != 0:
                count, tax = divmod(tax, coin)
                answer += count
        print(answer)


if __name__ == '__main__':
    main()

'''
4
200
700
7900
53200
'''