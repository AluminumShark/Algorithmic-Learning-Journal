# Time: O(N + (N-K) log N) (Heapify all, then pop excess)
# Space: O(N)
# Concept: Max-Heap based on distance.
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store (-distance, x, y) to simulate Max-Heap
        heap = [(-(x ** 2 + y ** 2), x, y) for x, y in points]
        heapq.heapify(heap)
        
        # Pop the "largest" distances until only k elements remain
        while len(heap) > k:
            heapq.heappop(heap)
            
        res = [[x, y] for _, x, y in heap]
        return res
