from typing import List

class Solution:
    """
    Intersection of Two Arrays
    Return a list of unique elements present in both arrays.

    Approach:
      1. Sort both arrays.
      2. Use two pointers to traverse them.
      3. If elements are equal, record it (avoid duplicates).
      4. Move the pointer(s) accordingly.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersect = []
        pt1, pt2 = 0, 0

        # Traverse both arrays using two pointers
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] == nums2[pt2]:
                # Avoid duplicates in result
                if not intersect or intersect[-1] != nums1[pt1]:
                    intersect.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:  # nums1[pt1] > nums2[pt2]
                pt2 += 1

        return intersect
