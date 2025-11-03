from typing import List

class MaxHeap:
    """
    Custom implementation of a Max Heap.
    Provides push() for insertion and pop() for extracting the maximum element.
    """

    def __init__(self):
        self.heap = []
    
    def _parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def _left(self, i: int) -> int:
        return 2 * i + 1
    
    def _right(self, i: int) -> int:
        return 2 * i + 2

    def push(self, val: int) -> None:
        # Insert new element and restore heap property upwards
        self.heap.append(val)
        self._heapifyUp(len(self.heap) - 1)

    def pop(self):
        # Remove and return the maximum element (root)
        if not self.heap:
            return None

        # Swap root with last element, remove last, then heapify down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_val = self.heap.pop()
        self._heapifyDown(0)
        return max_val
    
    def _heapifyUp(self, idx: int) -> None:
        # Restore heap property from bottom to top
        while idx > 0:
            parent = self._parent(idx)
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _heapifyDown(self, idx: int) -> None:
        # Restore heap property from top to bottom
        size = len(self.heap)
        while True:
            left, right = self._left(idx), self._right(idx)
            largest = idx
            
            # Compare with children and find the largest
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            
            # If the parent is smaller, swap and continue
            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break


class Solution:
    """
    Find the Kth largest element using a custom Max Heap.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = MaxHeap()
        result = None

        # Build the heap
        for num in nums:
            maxHeap.push(num)
        
        # Pop the largest element k times
        for _ in range(k):
            result = maxHeap.pop()
        
        return result
