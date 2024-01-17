class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row = Counter(tuple(row) for row in grid)
        for col in zip(*grid):
            ans += row[col]
        return ans
