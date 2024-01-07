class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        return max([min(citations[i], i + 1) for i in range(len(citations))])
