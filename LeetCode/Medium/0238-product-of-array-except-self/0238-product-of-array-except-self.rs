impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![1; nums.len()];
        let (mut prefix, mut postfix) = (1, 1);
        for i in 0..nums.len() {
            res[i] = prefix;
            prefix *= nums[i];
        }
        for i in (0..nums.len()).rev() {
            res[i] *= postfix;
            postfix *= nums[i];
        }
        res
    }
}
