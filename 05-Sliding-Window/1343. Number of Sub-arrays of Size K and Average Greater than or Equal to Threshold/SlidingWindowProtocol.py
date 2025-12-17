from typing import List

class Solution:
    """
    Number of Sub-arrays of Size K and Average ≥ Threshold
    Use a sliding window of fixed size k to maintain the sum dynamically.
    """

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        slow, fast = 0, 0
        windowSum = 0
        count = 0

        # Expand the window with fast pointer
        while fast < len(arr):
            windowSum += arr[fast]

            # When window size reaches k, check condition and slide
            if fast - slow + 1 == k:
                if windowSum / k >= threshold:
                    count += 1
                # Remove the element going out of the window
                windowSum -= arr[slow]
                slow += 1

            # Move fast pointer forward
            fast += 1

        return count
