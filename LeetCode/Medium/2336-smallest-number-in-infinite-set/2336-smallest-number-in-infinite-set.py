from heapq import heappush, heappop


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = list(range(1, 1001))

    def popSmallest(self) -> int:
        return heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num in self.heap:
            return
        return heappush(self.heap, num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)