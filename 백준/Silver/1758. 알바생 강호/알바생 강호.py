import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    li = [int(sys.stdin.readline().strip()) for _ in range(N)]
    li.sort(reverse=True)

    for i in range(N):
        li[i] = li[i] - i if li[i] >= i else 0

    print(sum(li))
