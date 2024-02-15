tribo = [0, 1, 1]


class Solution:
    def tribonacci(self, n: int) -> int:
        while len(tribo) <= n:
            tribo.append(sum(tribo[-3:]))
        return tribo[n]
