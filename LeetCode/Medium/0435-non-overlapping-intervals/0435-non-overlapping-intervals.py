import math


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        arrow = -math.inf
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= arrow:
                arrow = e
            else:
                ans += 1
        return ans
