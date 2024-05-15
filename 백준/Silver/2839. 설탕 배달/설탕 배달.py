import sys

input = sys.stdin.readline


def answer(N):
    answer = 0
    while N >= 0:
        if N % 5 == 0:
            answer += N // 5
            return answer
        N -= 3
        answer += 1
    return -1


if __name__ == "__main__":
    N = int(input())
    print(answer(N))
