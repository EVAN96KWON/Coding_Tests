def sort_by_count(lst):
    return sorted(list(set(lst)), key=lambda x: lst.count(x), reverse=True)


def solution(a, b, c, d):
    result = [a, b, c, d]
    len_result = len(set(result))

    if len_result == 1:
        return 1111 * result[-1]
    elif len_result == 2:
        p, q = sort_by_count(result)

        if result.count(p) == result.count(q):
            return (p + q) * abs(p - q)

        return (10 * p + q) ** 2
    elif len_result == 3:
        p, q, r = sort_by_count(result)
        return q * r
    elif len_result == 4:
        return min(result)
