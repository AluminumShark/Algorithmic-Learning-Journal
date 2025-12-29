from typing import Optional

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


# Solution 1: Hash Map (Two Passes)
# Time: O(n)
# Space: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            mp[cur].next = mp[cur.next]
            mp[cur].random = mp[cur.random]
            cur = cur.next
        return mp[head]


# Solution 2: Interweaving / Space Optimized (Three Passes)
# Time: O(n)
# Space: O(1) (excluding result)
# Concept: Interweave original and copy nodes (A->A'->B->B'), set random pointers, then separate.
class SolutionOptimized:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        # 1. Interweave nodes
        while cur:
            nxt = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = nxt
            cur = nxt
        
        # 2. Set Random pointers
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next

        # 3. Separate lists
        dummy = Node(0)
        copyTail = dummy
        cur = head
        while cur:
            copy = cur.next
            nxt = copy.next
            copyTail.next = copy
            copyTail = copy
            cur.next = nxt
            cur = nxt

        return dummy.next

