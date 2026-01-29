# Time: O(N) init, O(log K) add (Average case for heap operations)
# Space: O(K) (The heap stores K elements)
# Concept: Maintain a Min-Heap of size K. The root is the Kth largest.
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(nums)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
