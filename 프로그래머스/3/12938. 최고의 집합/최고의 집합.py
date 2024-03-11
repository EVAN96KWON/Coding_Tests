def solution(n, s):
    if s // n == 0:
        return [-1]

    avg, rem = divmod(s, n)
    return [avg] * (n - rem) + [avg + 1] * rem
