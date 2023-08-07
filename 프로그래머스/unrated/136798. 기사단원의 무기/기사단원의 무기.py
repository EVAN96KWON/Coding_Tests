def build_divisors(maximum):
    div = [0] * (maximum + 1)
    for i in range(1, maximum + 1):
        for j in range(i, maximum + 1, i):
            div[j] += 1
    return div


div = build_divisors(100001)


def solution(number, limit, power):
    global div
    answer = []
    for i in range(1, number + 1):
        _power = div[i]
        answer.append(_power if _power <= limit else power)
    return sum(answer)
