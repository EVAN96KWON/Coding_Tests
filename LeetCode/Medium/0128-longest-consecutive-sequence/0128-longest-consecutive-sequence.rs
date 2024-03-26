use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<i32> = HashSet::from_iter(nums);
        let mut longest = 0;
        num_set.iter().for_each(|num| {
            if !num_set.contains(&(num - 1)) {
                let mut len = 0;
                while num_set.contains(&(num + len)) {
                    len += 1;
                }
                longest = longest.max(len);
            }
        });
        longest
    }
}
