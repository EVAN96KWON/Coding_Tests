class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        queue: deque[tuple[int, int, int]] = deque([(start_row, start_col, 0)])

        while queue:
            row, col, steps = queue.popleft()

            if row in (0, m - 1) or col in (0, n - 1):
                if row != start_row or col != start_col:
                    return steps

                if maze[row][col] != "+":
                    return steps

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy

                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and maze[new_row][new_col] == "."
                ):
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, steps + 1))

        return -1
