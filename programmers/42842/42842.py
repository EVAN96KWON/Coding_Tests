def solution(brown, yellow):
    w_plus_h = int(brown // 2) - 2

    for i in range(1, w_plus_h + 1):
        w = i
        h = w_plus_h - i
        if w * h == yellow:
            return [w + 2, h + 2]


if __name__ == '__main__':
    print(solution(10, 2))  # [4, 3]
    print(solution(8, 1))  # [3, 3]
    print(solution(24, 24))  # [8, 6]
