use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        nums.into_iter().for_each(|x| heap.push(x));
        (0..k - 1).for_each(|_| { heap.pop(); });
        heap.pop().unwrap()
    }
}
