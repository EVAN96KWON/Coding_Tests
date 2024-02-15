class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        while len(dp) < len(cost):
            dp.append(cost[len(dp)] + min(dp[-1], dp[-2]))

        return min(dp[-1], dp[-2])
