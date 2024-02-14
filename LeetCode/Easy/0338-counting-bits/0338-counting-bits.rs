impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut v = vec![0; n as usize + 1];
        for i in 1..=n {
            v[i as usize] = v[i as usize / 2] + i % 2;
        }
        v
    }
}
