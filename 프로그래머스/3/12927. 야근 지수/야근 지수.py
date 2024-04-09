from heapq import heapify, heappush, heappop


def solution(n, works):
    heapify(works := [-x for x in works])
    for _ in range(min(n, -1 * sum(works))):
        heappush(works, heappop(works) + 1)
    return sum(map(lambda x: x**2, works))
