def solution(sizes):
    x_sizes, y_sizes = [], []

    for s in sizes:
        s.sort()
        x_sizes.append(s[0])
        y_sizes.append(s[1])

    return max(x_sizes) * max(y_sizes)


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    # 4000
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    # 120
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
    # 133
