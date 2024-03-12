impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let mut visited = vec![false; is_connected.len()];
        let mut count = 0;

        for i in 0..is_connected.len() {
            if !visited[i] {
                Self::dfs(&is_connected, &mut visited, i);
                count += 1
            }
        }
        count
    }

    fn dfs(is_connected: &Vec<Vec<i32>>, visited: &mut Vec<bool>, i: usize) {
        visited[i] = true;
        for (n, &c) in is_connected[i].iter().enumerate() {
            if c == 1 && !visited[n] {
                Self::dfs(is_connected, visited, n);
            }
        }
    }
}

