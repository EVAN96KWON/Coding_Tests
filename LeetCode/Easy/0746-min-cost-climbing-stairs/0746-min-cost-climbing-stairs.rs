impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut dp = Vec::from([cost[0], cost[1]]);
        for i in 2..cost.len() {
            dp.push(cost[i] + dp[i - 1].min(dp[i - 2]))
        }
        dp[dp.len() - 1].min(dp[dp.len() - 2])
    }
}
