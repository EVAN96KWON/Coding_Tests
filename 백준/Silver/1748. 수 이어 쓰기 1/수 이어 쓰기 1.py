if __name__ == '__main__':
    N = input()
    l = len(N) - 1
    count = 0
    for i in range(l):
        count += 9 * (10 ** i) * (i + 1)
    count += ((int(N) - (10 ** l) + 1) * (l + 1))
    print(count)

