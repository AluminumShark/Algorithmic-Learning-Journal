from typing import List

class Solution:
    """
    Remove Duplicates from Sorted Array (in-place)
    Given a sorted array, remove duplicates so that each unique element
    appears only once. Return the new length.
    
    Approach:
      - Use two pointers: `slow` marks the end of the unique section,
        `fast` scans ahead for the next distinct element.
      - Whenever a new unique number is found, expand the unique section.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: empty list
        if not nums:
            return 0

        slow, fast = 0, 1

        # Move `fast` pointer to find next distinct value
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                # Found a new unique element
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1
        
        # Return the length of unique elements (index + 1)
        return slow + 1
