def get_minus_binary(N):
    if N == 0:
        return "0"
    n = N
    rst = ""
    while n:
        if n % -2:
            rst = '1' + rst
            n = n // -2 + 1
        else:
            rst = '0' + rst
            n = n // -2
    return rst


if __name__ == '__main__':
    N = int(input())
    print(get_minus_binary(N))

