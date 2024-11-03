def solution(diffs, times, limit):
    def solve_by_level(level):
        return sum(
            [
                (p + t) * max(0, (d - level)) + t
                for d, t, p in zip(diffs, times, prev_times)
            ]
        )

    answer = 0
    prev_times = [0] + times

    left, right = 1, max(diffs) + 1
    while left < right:
        mid = (left + right) // 2
        if solve_by_level(mid) <= limit:
            answer = mid
            right = mid
        else:
            left = mid + 1

    return answer
