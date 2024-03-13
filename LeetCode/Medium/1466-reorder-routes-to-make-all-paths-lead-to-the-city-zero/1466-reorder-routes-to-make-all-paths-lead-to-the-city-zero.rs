impl Solution {
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let mut graph = vec![vec![]; n as usize];
        for edge in connections {
            let (s, e) = (edge[0], edge[1]);
            graph[s as usize].push((e, 1));
            graph[e as usize].push((s, 0));
        }

        let mut res = 0;
        let mut queue = std::collections::VecDeque::new();
        let mut visited = vec![0; n as usize];
        queue.push_back((0, 0));

        while let Some((node, can_reach)) = queue.pop_front() {
            visited[node] = 1;
            res += can_reach as i32;

            for (e, can_reach) in &graph[node] {
                let e = *e as usize;
                if visited[e] == 0 {
                    queue.push_back((e, *can_reach));
                }
            }
        }

        res
    }
}
