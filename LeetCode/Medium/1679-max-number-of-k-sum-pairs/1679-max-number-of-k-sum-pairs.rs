impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let (mut i, mut j) = (0, nums.len() - 1);
        let mut res = 0;
        let mut _nums = nums.clone();
        _nums.sort();
        while i < j {
            if _nums[i] + _nums[j] < k {
                i += 1;
            } else if _nums[i] + _nums[j] > k {
                j -= 1;
            } else {
                res += 1;
                i += 1;
                j -= 1;
            }
        }
        res   
    }
}