from typing import List

class Solution:
    """
    Merge Sorted Array (In-place, from the end)
    Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    nums1 has enough space at the end to hold additional elements.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers:
        # i → last initialized element in nums1
        # j → last element in nums2
        # k → last overall index in nums1
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge from the end to the beginning
        while i >= 0 and j >= 0:
            # Choose the larger element and put it at position k
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If any elements remain in nums2, copy them over
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
