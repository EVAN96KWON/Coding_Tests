from heapq import heappush, heappop


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        min_heap = []
        total = res = 0

        for n1, n2 in sorted(zip(nums1, nums2), key=lambda x: -x[1]):
            total += n1
            heappush(min_heap, n1)
            if len(min_heap) == k:
                res = max(res, total * n2)
                total -= heappop(min_heap)
        return res
