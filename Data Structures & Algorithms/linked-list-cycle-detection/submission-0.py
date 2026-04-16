# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Define a function that takes head (the first node of the linked list) as input

        # Step 2: Initialize two pointers: slow and fast
        # slow starts at head, fast also starts at head
        slow = head
        fast = head

        # Step 3: While fast and fast.next are not None
        while fast and fast.next:
            
            # Step 3.1: Move slow one step forward (slow = slow.next)
            slow = slow.next
            # Step 3.2: Move fast two steps forward (fast = fast.next.next)
            fast = fast.next.next
            # Step 3.3: If slow and fast meet at the same node, return True (cycle detected)
            if slow == fast:
                return True

        # Step 4: If loop ends, return False (no cycle)
        return False
