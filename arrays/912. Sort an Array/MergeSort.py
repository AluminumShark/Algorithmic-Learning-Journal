from typing import List

class Solution:
    """
    Merge Sort (Efficient O(n log n) Divide & Conquer Algorithm)
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        # Entry point — call the recursive merge sort function
        return self.mergeSort(nums)

    def mergeSort(self, arr):
        # Base case: arrays with 0 or 1 element are already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide step: split the array into two halves
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        # Conquer step: merge the sorted halves
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i, j = 0, 0

        # Merge two sorted lists into one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Append any remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result
