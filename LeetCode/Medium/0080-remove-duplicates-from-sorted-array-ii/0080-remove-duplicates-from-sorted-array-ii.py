from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rm = nums.copy()
        d = defaultdict(int)
        for i in rm:
            d[i] += 1
        for i in d:
            while d[i] > 2:
                rm.remove(i)
                d[i] -= 1
        nums[:] = rm + ["_"] * (len(nums) - len(rm))
        return len(rm)
