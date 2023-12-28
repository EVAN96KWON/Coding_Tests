class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = [n for n in nums if n != val]
        nums[:] = removed + ["_"] * (len(nums) - len(removed))
        return len(removed)
