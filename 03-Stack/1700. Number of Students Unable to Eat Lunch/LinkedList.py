from typing import List

class ListNode:
    def __init__(self, val, next=None):
        self.val = val      # Student preference (0: circular, 1: square)
        self.next = next    # Link to the next student in the queue

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Step 1: Build a linked list to simulate the student queue
        head = tail = ListNode(-1)      # Dummy head for simplicity
        for s in students:
            node = ListNode(s)
            tail.next = node
            tail = node

        size = len(students)            # Current number of students
        i = 0                           # Index in sandwiches array
        rotate = 0                      # Tracks consecutive rotations (no one taking a sandwich)
        
        # Step 2: Process until all sandwiches are served or no one wants the current sandwich
        while head.next and i < len(sandwiches):
            front = head.next            # The student at the front of the queue
        
            if front.val == sandwiches[i]:
                # Student takes the sandwich → remove from queue
                head.next = front.next
                if front is tail:
                    tail = head          # Queue becomes empty
                size -= 1
                i += 1                   # Move to next sandwich
                rotate = 0               # Reset rotation counter
            else:
                # Student refuses the sandwich → move to back
                if rotate == size:
                    # If everyone has refused once, process stops
                    break

                head.next = front.next   # Remove from front
                front.next = None
                tail.next = front        # Append to back
                tail = front
                rotate += 1              # Count one full rotation

        return size                      # Number of students who cannot eat
