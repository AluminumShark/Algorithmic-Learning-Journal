from typing import List
from collections import Counter
import heapq

# Solution 1: Sorting (O(nlogn))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        count = list(count.items())
        count.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            key, _ = count[i]
            ans.append(key)
        return ans


# Solution 2: Counter
class SolutionCounter:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        res = ctr.most_common(k)
        return [n for n, _ in res]


# Solution 3: Heap (O(nlogk))
class SolutionHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        heap = []
        for num, freq in ctr.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]

