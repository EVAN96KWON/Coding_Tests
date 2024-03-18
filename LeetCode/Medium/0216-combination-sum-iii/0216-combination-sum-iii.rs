impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut res = vec![];
        Self::backtrack(1, &mut vec![], n, &mut res, k);
        res
    }

    fn backtrack(
        start: i32,
        combination: &mut Vec<i32>,
        target: i32,
        res: &mut Vec<Vec<i32>>,
        k: i32,
    ) {
        if combination.len() == k as usize && target == 0 {
            res.push(combination.clone());
            return;
        }

        if combination.len() as i32 > k || target < 0 {
            return;
        }

        for i in start..10 {
            combination.push(i);
            Self::backtrack(i + 1, combination, target - i, res, k);
            combination.pop();
        }
    }
}
