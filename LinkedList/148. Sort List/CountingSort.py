from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    """
    Counting Sort on Linked List
    Works efficiently only when node values are integers within a small range.
    """

    def countingSort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Find min and max values in the list
        listMin, listMax = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < listMin:
                listMin = cur.val
            if cur.val > listMax:
                listMax = cur.val
            cur = cur.next
        
        # Step 2: Initialize counting array for range [listMin, listMax]
        size = listMax - listMin + 1
        counts = [0 for _ in range(size)]

        # Step 3: Count occurrences of each value
        cur = head
        while cur:
            counts[cur.val - listMin] += 1
            cur = cur.next
        
        # Step 4: Rebuild a new sorted linked list
        dummyHead = ListNode(-1)
        cur = dummyHead
        for i in range(size):
            while counts[i] > 0:
                newNode = ListNode(i + listMin)
                cur.next = newNode
                cur = cur.next
                counts[i] -= 1

        return dummyHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.countingSort(head)
