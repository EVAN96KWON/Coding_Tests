class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        len_nums_set = len(num_set)
        for num in nums:
            num_set.add(num)

            if len(num_set) == len_nums_set:
                return num

            len_nums_set += 1
        return -1
