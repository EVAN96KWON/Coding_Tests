def solution(n, arr1, arr2):
    result = [''.join(
        ['#' if k == '1' else ' ' for j in str(bin(i[0] | i[1]))[2:].rjust(n, '0') for k in j]
    ) for i in zip(arr1, arr2)]
    return result


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
