arr = [0] * 1000001


def init_arr(n):
    a = [0] * 1000001
    a[1] = 0
    for i in range(2, n + 1):
        a[i] = a[i - 1] + 1
        if i % 2 == 0:
            a[i] = min(a[i], a[int(i/2)] + 1)
        if i % 3 == 0:
            a[i] = min(a[i], a[int(i/3)] + 1)
    return a


if __name__ == '__main__':
    X = int(input())
    arr = init_arr(X)
    print(arr[X])
