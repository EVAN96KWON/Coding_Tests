import heapq


def solution(scoville, K):
    cnt = 0
    heap = []
    heapq.heapify()
    for _ in scoville:
        heapq.heappush(heap, _)

    while heap[0] < K and len(heap) > 1:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1

    return cnt if heap[0] > K else -1


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
