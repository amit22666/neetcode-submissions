# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Define a function that takes two linked list heads (list1 and list2) as input

        # Step 2: Create a dummy node (a placeholder node) to build the result list
        dummy_node = ListNode() 
        current = dummy_node
        # Step 2.1: Initialize a pointer current pointing to dummy 
        # (this will help us attach nodes one by one)

        # Step 3: While both list1 and list2 are not None
        while list1 and list2:
            # Step 3.1: Compare the values at list1 and list2

            # Step 3.2: If list1’s value is smaller or equal
            if list1.val <= list2.val:
                current.next = list1
                # Attach list1 node to current.next
                # Move list1 forward (list1 = list1.next)
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2
        
        return dummy_node.next


            # Step 3.3: Else (list2’s value is smaller)
                # Attach list2 node to current.next
                # Move list2 forward (list2 = list2.next)
            # Step 3.4: Move current forward (current = current.next)

        # Step 4: After the loop, one of the lists might still have remaining nodes
        # Step 4.1: Attach whichever list is not None directly to current.next

        # Step 5: Return dummy.next (because dummy was just a placeholder)

        