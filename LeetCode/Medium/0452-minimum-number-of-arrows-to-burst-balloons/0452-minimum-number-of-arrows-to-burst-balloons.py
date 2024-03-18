class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        arros_pos = points[0][1]

        for s, e in points:
            if s > arros_pos:
                arrows += 1
                arros_pos = e

        return arrows
