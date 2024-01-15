use std::collections::{HashMap, HashSet};


impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut counts = HashMap::new();

        for n in arr {
            let count = counts.entry(n).or_insert(0);
            *count += 1;
        }

        counts.values().collect::<HashSet<_>>().len() == counts.len()
    }
}
