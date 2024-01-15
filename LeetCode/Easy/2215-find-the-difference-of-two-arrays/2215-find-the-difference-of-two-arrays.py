class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        _set1 = set(nums1)
        _set2 = set(nums2)
        return [list(_set1 - _set2), list(_set2 - _set1)]
