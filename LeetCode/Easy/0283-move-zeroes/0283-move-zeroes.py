class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [n for n in nums if n != 0]
        nums[:] = res + [0] * (len(nums) - len(res))
