impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let (m, n) = (maze.len() as i32, maze[0].len() as i32);
        let (start_row, start_col) = (entrance[0], entrance[1]);
        let mut maze = maze;
        maze[start_row as usize][start_col as usize] = '+';
        let mut queue = std::collections::VecDeque::from(vec![(start_row, start_col, 0)]);

        while let Some((row, col, steps)) = queue.pop_front() {
            if row == 0 || row == m - 1 || col == 0 || col == n - 1 {
                if row != start_row || col != start_col {
                    return steps;
                }

                if maze[row as usize][col as usize] != '+' {
                    return steps;
                }
            }

            for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)] {
                let (new_row, new_col) = (row + dx, col + dy);

                if (0 <= new_row && new_row < m)
                    && (0 <= new_col && new_col < n)
                    && maze[new_row as usize][new_col as usize] == '.'
                {
                    maze[new_row as usize][new_col as usize] = '+';
                    queue.push_back((new_row, new_col, steps + 1));
                }
            }
        }

        return -1;
    }
}
