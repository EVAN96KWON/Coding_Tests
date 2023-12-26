def solution(n, arr1, arr2):
    return [''.join([bin(i[0] | i[1])[2:].rjust(n, '0').replace('1', '#').replace('0', ' ')]) for i in zip(arr1, arr2)]


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
