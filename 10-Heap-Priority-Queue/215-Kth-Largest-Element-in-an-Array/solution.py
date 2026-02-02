# Time: O(N log K)
# Space: O(K)
# Concept: Min-Heap of size K.
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
