class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = self.find_rotten(grid)
        visited = set(rotten)
        queue = [(r, c, 0) for r, c in rotten]
        steps = 0

        while queue:
            r, c, steps = queue.pop(0)
            visited.add((r, c))
            grid[r][c] = 2

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if self.is_valid(grid, nr, nc) and (nr, nc) not in visited:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, steps + 1))

        if any(1 in row for row in grid):
            return -1

        return steps

    def find_rotten(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        return [
            (r, c)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            if val == 2
        ]

    def is_valid(self, grid: List[List[int]], r: int, c: int) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1