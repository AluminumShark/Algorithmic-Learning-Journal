from typing import List

class Solution:
    """
    Relative Sort Array using Counting Sort.
    Sort arr1 such that:
      - Elements appearing in arr2 come first, in the same order as arr2.
      - Remaining elements (not in arr2) are placed at the end in ascending order.

    Counting Sort is efficient here because element values are bounded (0–1000).
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Step 1. Determine value range
        arr1Max, arr1Min = max(arr1), min(arr1)
        size = arr1Max - arr1Min + 1
        count = [0 for _ in range(size)]

        # Step 2. Count frequency of each number in arr1
        for num in arr1:
            count[num - arr1Min] += 1
        
        result: List[int] = []

        # Step 3. Place elements that appear in arr2 first (respecting arr2 order)
        for num in arr2:
            while count[num - arr1Min] > 0:
                result.append(num)
                count[num - arr1Min] -= 1
            
        # Step 4. Append remaining elements (not in arr2) in ascending order
        for i in range(size):
            while count[i] > 0:
                num = i + arr1Min
                result.append(num)
                count[i] -= 1
        
        return result
