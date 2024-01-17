use std::collections::HashMap;

impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        let mut rows = HashMap::new();
        for row in grid.iter() {
            *rows.entry(row).or_insert(0) += 1;
        }

        for i in 0..grid.len() {
            let mut col = Vec::new();
            for j in 0..grid.len() {
                col.push(grid[j][i]);
            }

            if rows.contains_key(&col) {
                ans += rows[&col];
            }
        }

        return ans;
    }
}
