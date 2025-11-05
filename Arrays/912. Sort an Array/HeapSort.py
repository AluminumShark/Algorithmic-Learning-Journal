from typing import List

class MinHeap:
    def __init__(self):
        # Underlying array to store heap elements
        self.heap = []
    
    def _parent(self, i: int) -> int:
        # Index of the parent node
        return (i - 1) // 2
    
    def _left(self, i: int) -> int:
        # Index of the left child
        return 2 * i + 1
    
    def _right(self, i: int) -> int:
        # Index of the right child
        return 2 * i + 2

    def peek(self):
        # Return the minimum element without removing it
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, val: int) -> None:
        # Insert at the end and bubble up (heapify up)
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove and return the minimum element (root)
        if not self.heap:
            return None
        
        # Move last element to root, shrink, then heapify down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, idx: int) -> None:
        # Restore heap property upward from index `idx`
        while idx > 0:
            parent = self._parent(idx)
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _heapify_down(self, idx: int) -> None:
        # Restore heap property downward from index `idx`
        size = len(self.heap)
        while True:
            left, right = self._left(idx), self._right(idx)
            smallest = idx
            
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

class Solution:
    """
    Heap Sort using a custom MinHeap:
    - Push all numbers into the min-heap
    - Pop elements one by one to get sorted order
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = MinHeap()
        result: List[int] = []

        # Build heap: O(n log n) with repeated insertions
        for value in nums:
            heap.push(value)

        # Extract min n times to form the sorted array
        while heap.heap:
            result.append(heap.pop())

        return result
