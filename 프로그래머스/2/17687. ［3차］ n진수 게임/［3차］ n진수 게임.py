def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    num = "".join([convert(i, n) for i in range(t * m)])
    return num[p - 1 :: m][:t]
