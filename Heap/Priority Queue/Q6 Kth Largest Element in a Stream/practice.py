import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


number = KthLargest(4, [12,6])
number.add(5)
number.add(10)
number.add(65)

