# Time: O(N log N)
# Space: O(N)
# Concept: Max-Heap Simulation (using negative values). Pop two largest, push difference.
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heap is min-heap, so we negate values to simulate max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x1 = heapq.heappop(heap) # Largest
            x2 = heapq.heappop(heap) # Second largest
            if x1 == x2:
                continue
            else:
                heapq.heappush(heap, -abs(x1 - x2))
        return -heap[0] if heap else 0
