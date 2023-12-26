def solution(lst):
    x1, y1, r1, x2, y2, r2 = lst
    d_pow = (pow(x1 - x2, 2) + pow(y1 - y2, 2))

    # 일치하면 -1
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    if pow(r1 - r2, 2) < d_pow < pow(r1 + r2, 2):
        return 2
    elif d_pow == pow(r1 - r2, 2) or d_pow == pow(r1 + r2, 2):
        return 1
    else:
        return 0


if __name__ == '__main__':
    N = int(input())
    case_list = [list(map(float, input().split())) for _ in range(N)]

    for case in case_list:
        print(solution(case))

