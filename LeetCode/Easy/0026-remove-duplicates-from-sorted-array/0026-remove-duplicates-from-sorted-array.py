class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = sorted(list(set(nums)))
        nums[:] = removed + ["_"] * (len(nums) - len(removed))
        return len(removed)
