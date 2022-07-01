def main():
    for t in range(int(input())):
        n = int(input())
        steps = [0] + list(map(int, input().split()))

        if n == 1:
            print(steps[-1])
            continue
        elif n == 2:
            print(max(steps[2], steps[1] + steps[2]))
            continue

        steps[0] = 0
        steps[2] += max(steps[0], steps[1])
        for i in range(3, n + 1):
            if i % 3 == 0:
                steps[i] += max(steps[i - 1], steps[i - 2], steps[i // 3])
            else:
                steps[i] += max(steps[i - 1], steps[i - 2])

        print(steps[-1])


if __name__ == '__main__':
    main()

'''
7
1
-13
2
3 -3
2
-4 -2
4
10 20 30 40
8
3 5 -6 -1 -9 11 -12 10
9
6 -3 9 -2 7 -1 -4 -2 4
10
10 -1 10 -1 -1 -1 -1 -1 10 -1
'''