from typing import List

# Solution 1: Brute Force
# Time: O(max(p) * len(p))
# Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = max(piles)
        for k in range(1, maxP + 1):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours <= h:
                return k


# Solution 2: Binary Search on Answer
# Time: O(len(p) * log(max(p)))
# Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        ans = 0
        while L <= R:
            k = (L + R) // 2
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours > h:
                L = k + 1
            else:
                ans = k
                R = k - 1
        return ans

