from heapq import heapify, heappush, heappop


def solution(n, works):
    works = [-x for x in works]
    heapify(works)
    for _ in range(n):
        max_work = heappop(works)
        if max_work == 0:
            break
        max_work += 1
        heappush(works, max_work)

    return sum(map(lambda x: x**2, works))
