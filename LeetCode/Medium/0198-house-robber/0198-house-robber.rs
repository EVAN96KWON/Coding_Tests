impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut prev, mut prevprev) = (0, 0);

        for n in nums {
            let tmp = prev.max(n + prevprev);
            prevprev = prev;
            prev = tmp;
        }

        prev
    }
}
