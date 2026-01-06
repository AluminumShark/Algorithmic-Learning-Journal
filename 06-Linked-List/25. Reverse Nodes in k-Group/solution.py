# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# Solution: Iterative Group Reversal
# ============================================================
# Time: O(n) - each node is visited twice (once to count, once to reverse)
# Space: O(1) - only pointer manipulation, no extra data structures
#
# Concept: Reverse Linked List in Chunks
# --------------------------------------
# For each group of k nodes:
# 1. Find the kth node (if fewer than k remain, we're done)
# 2. Reverse the group in-place
# 3. Connect the reversed group to the previous part
# 4. Move to the next group
#
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy  # Node before the current group

        while True:
            # Step 1: Find the kth node from groupPrev
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # Fewer than k nodes remaining, we're done
                    return dummy.next

            # Save the node after this group
            groupNext = kth.next

            # Step 2: Reverse the group [groupPrev.next ... kth]
            # Standard linked list reversal
            groupStart = groupPrev.next
            prev = groupNext  # After reversal, first node points to groupNext
            cur = groupStart

            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Step 3: Connect the reversed group
            # After reversal:
            # - kth is now the first node of the reversed group
            # - groupStart is now the last node of the reversed group
            groupPrev.next = kth       # Connect previous part to new first
            groupPrev = groupStart     # Move to end of reversed group (new groupPrev)

        # Note: The return happens inside the loop when we find < k nodes

