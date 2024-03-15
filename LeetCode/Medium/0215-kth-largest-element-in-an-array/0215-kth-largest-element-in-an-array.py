class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while nums and len(nums) > k:
            heappop(nums)
        return nums[-k]
