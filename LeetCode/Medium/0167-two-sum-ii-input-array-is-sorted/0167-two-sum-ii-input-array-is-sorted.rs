impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut left, mut right) = (0, numbers.len() - 1);
        while left < right {
            let cur = numbers[left] + numbers[right];
            match cur.cmp(&target) {
                std::cmp::Ordering::Less => left += 1,
                std::cmp::Ordering::Greater => right -= 1,
                std::cmp::Ordering::Equal => return vec![left as i32 + 1, right as i32 + 1],
            }
        }
        vec![]
    }
}
