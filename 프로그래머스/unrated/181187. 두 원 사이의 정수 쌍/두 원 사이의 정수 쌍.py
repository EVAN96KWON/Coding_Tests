import math


def solution(r1, r2):
    count = 0
    for x in range(1, r2 + 1):
        upper = math.floor(math.sqrt(r2**2 - x**2))
        lower = 0 if x >= r1 else math.ceil(math.sqrt(r1**2 - x**2))
        count += upper - lower + 1
    return count * 4
