from typing import List

# Solution 1: Brute Force (Merge and Sort)
# Time: O((m+n) * log(m+n))
# Space: O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n % 2 == 1:
            return float(nums3[n // 2])
        else:
            return (nums3[n // 2 - 1] + nums3[n // 2]) / 2.0


# Solution 2: Binary Search (Optimal Partitioning)
# Time: O(log(min(m, n)))
# Space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        total = m + n
        leftSize = total // 2

        L, R = 0, m
        while L <= R:
            i = (L + R) // 2
            j = leftSize - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
        
            if Aleft > Bright:
                R = i - 1
            else:
                L = i + 1

