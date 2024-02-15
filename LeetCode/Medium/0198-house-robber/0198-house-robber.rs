impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut prev, mut prevprev) = (0, 0);

        for n in nums {
            (prev, prevprev) = (prev.max(n + prevprev), prev);
        }

        prev
    }
}
