use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freq = HashMap::new();
        let mut result = vec![];
        for num in nums {
            freq.entry(num).and_modify(|x| *x += 1).or_insert(1);
        }
        for (_k, _) in freq.into_iter() {
            result.push(_k);
            if result.len() == k as usize {
                break;
            }
        }
        result
    }
}
