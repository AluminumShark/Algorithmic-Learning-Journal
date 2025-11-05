from typing import List

class Solution:
    """
    Two Sum II — Find two numbers that add up to a specific target in a sorted array.

    Approach:
      - Use two pointers: one starting at the left end, one at the right end.
      - Move inward based on comparison with the target sum.
      - Since the array is sorted, this ensures O(n) time.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        # Move pointers toward each other
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Return 1-indexed positions as per problem statement
                return [left + 1, right + 1]
            elif current_sum < target:
                # Need a larger sum → move left pointer rightward
                left += 1
            else:
                # Need a smaller sum → move right pointer leftward
                right -= 1
