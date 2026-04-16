# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Core idea (your thought process is correct)
        # For each pair of nodes:

        # Take values from l1 and l2 (use 0 if a list ended).
        # Add them together + any existing carry.
        # Create a new node with sum % 10.
        # Carry becomes sum // 10.
        # Move to the next nodes in both lists.
        # After the loop, if carry > 0, append a final node.

        # I REMEMBERED carry should be there in while loop condition
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

            
