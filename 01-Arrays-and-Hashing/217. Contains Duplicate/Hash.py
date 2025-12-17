from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = dict()               # Dictionary to record seen numbers
        
        for num in nums:
            if num in numDict:          # If number already exists, it's a duplicate
                return True
            else:
                numDict[num] = num      # Mark number as seen
        
        return False                    # No duplicates found
