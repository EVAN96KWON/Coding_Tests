impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let mut visited = vec![false; is_connected.len()];
        let mut count = 0;
        let mut queue = vec![];

        for i in 0..is_connected.len() {
            if !visited[i] {
                count += 1;
                queue.push(i);
            }

            while !queue.is_empty() {
                let j = queue.pop().unwrap();
                visited[j] = true;

                for k in 0..is_connected.len() {
                    if is_connected[j][k] == 1 && !visited[k] {
                        visited[k] = true;
                        queue.push(k);
                    }
                }
            }
        }

        count
    }
}
