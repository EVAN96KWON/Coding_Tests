class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        arrow = intervals.pop(0)[1]
        for s, e in intervals:
            if s >= arrow:
                arrow = e
            else:
                ans += 1
        return ans
