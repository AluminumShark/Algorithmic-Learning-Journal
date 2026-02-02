# Solution 1: Sorting (Brute Force)
# Time: O(N log N) for addNum
# Space: O(N)

class MedianFinderSort:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            idx1 = len(self.nums) // 2
            idx2 = idx1 - 1
            return (self.nums[idx1] + self.nums[idx2]) / 2
        else:
            idx = len(self.nums) // 2
            return self.nums[idx]


# Solution 2: Two Heaps (Max-Heap + Min-Heap)
# Time: O(log N) per add, O(1) find. (Total O(N log N))
# Space: O(N)
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max-Heap (stored as negative)
        self.large = []  # Min-Heap

    def addNum(self, num: int) -> None:
        # Always push to small first
        heapq.heappush(self.small, -num)

        # Ensure all elements in small are <= all elements in large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the sizes (small should have at most 1 more element than large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
