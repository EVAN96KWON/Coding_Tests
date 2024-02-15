impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut tribo = vec![0, 1, 1];
        while tribo.len() < n as usize + 1 {
            tribo.push(tribo[tribo.len() - 1] + tribo[tribo.len() - 2] + tribo[tribo.len() - 3]);
        }
        tribo[n as usize]
    }
}
