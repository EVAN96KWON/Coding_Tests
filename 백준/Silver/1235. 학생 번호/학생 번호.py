import sys


# check
def check(N, list, s):
    for i in range(N):
        for j in range(i + 1, N):
            if list[i][-s:] == list[j][-s:]:
                return False
    return True


def solution(N, list):
    for i in range(1, len(list[0])):
        if check(N, list, i):
            return i
    return len(list[0])


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    list = [sys.stdin.readline().strip() for _ in range(N)]

    print(solution(N, list))
