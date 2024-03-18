class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, combination: List[int], target: int) -> None:
            if len(combination) == k and target == 0:
                result.append(combination.copy())
                return
            if len(combination) == k or target < 0:
                return
            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, combination, target - i)
                combination.pop()

        backtrack(1, [], n)
        return result
