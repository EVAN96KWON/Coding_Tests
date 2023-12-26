def solution(numbers):
    return [(n | ~n & (n + 1)) & ~((~n & (n + 1)) >> 1) for n in numbers]


if __name__ == '__main__':
    print(solution([2, 7]))  # [3, 11]
    print(solution([2, 10 ** 15]))  # [3, 11]
