from collections import deque


def solution(A, B):
    cnt = 0
    A = deque(sorted(A))
    B = deque(sorted(B))
    while B:
        if A[0] < B[0]:
            cnt += 1
            A.popleft()
        B.popleft()
    return cnt
