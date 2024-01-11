impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let (mut left, mut right): (usize, usize) = (0, 0);
        let mut k = 1;

        for i in 0..nums.len() {
            if nums[i] == 0 {
                k -= 1;
            }
            if k < 0 {
                if nums[left] == 0 {
                    k += 1;
                }
                left += 1;
            }
            right = i;
        }

        return right as i32 - left as i32;
    }
}
