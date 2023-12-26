if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = 0

    while B:
        max_B = max(B)
        min_A = min(A)
        answer += min_A * max_B
        B.remove(max_B)
        A.remove(min_A)

    print(answer)
