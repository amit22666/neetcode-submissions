# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Define a function that takes head (the first node of the linked list) as input

        # Step 2: Initialize a variable prev as None 
        # (this will eventually become the new head)
        prev = None

        # Step 3: Initialize a variable curr as head 
        # (to start traversing the list from the beginning)
        curr = head

        # Step 4: While curr is not None (loop through the list)
        while curr != None:
            # Step 4.1: Store the next node in a variable next_node = curr.next 
            # (so we don’t lose the rest of the list)
            next_node = curr.next

            # Step 4.2: Reverse the pointer of the current node: curr.next = prev
            curr.next = prev
            # Step 4.3: Move prev forward: prev = curr
            prev = curr
            # Step 4.4: Move curr forward: curr = next_node
            curr = next_node
        # Step 5: After the loop, prev will point to the new head of the reversed list

        # Step 6: Return prev as the new head
        return prev
        