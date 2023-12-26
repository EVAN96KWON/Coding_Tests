
zeros = [1, 0]
ones = [0, 1]


def fibonacci(n):
    length = len(zeros)
    if n >= length:
        for i in range(length, n + 1):
            zeros.append(zeros[i - 1] + zeros[i - 2])
            ones.append(ones[i - 1] + ones[i - 2])
    print(zeros[n], ones[n])


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        fibonacci(int(input()))
