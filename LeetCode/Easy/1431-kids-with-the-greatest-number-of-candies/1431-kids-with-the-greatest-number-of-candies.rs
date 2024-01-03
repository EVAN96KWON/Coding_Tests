impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let _max = *candies.iter().max().unwrap();
        let mut result = vec![];
        for i in 0..candies.len() {
            result.push(candies[i] + extra_candies >= _max);
        }
        result
    }
}