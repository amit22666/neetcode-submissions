# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Dummy node to simplify removal (including when we remove the head)
        dummy = ListNode(0, head)

        fast = dummy
        slow = dummy
        temp_n = n
        while temp_n>0:
            fast = fast.next
            temp_n = temp_n-1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow.next:
            slow.next = slow.next.next
        return dummy.next

        # Please tell if i'm thinking in the right directio or not
        # we have to delete nth node from the end it means we have to delete 
        # (len of linked list) - n from the front
        # now i have delete this node from front
# --------------------------------
#  THIS IS A 2 PASS APPROACH - OPTIMAL ONE PASS
#         But computing the length first means:

            # Traverse list → compute length
            # Traverse again → delete node

            # This is valid but not optimal 

# --------------------------------
# SOCHNE KA TARIKA THODA ALAG HAI ISMEIN
# INITIALLY 
# MEIN FAST KO N POSITION AAGE RAKH DUNGA SLOW SE
# AB POINTERS KO AGGE BHADAE - KEEPING THIS WINDOW SIZE FIXED
# JAB FAST WALA POINTER END MEIN HOGA TOH SLOW WALA POINTER N POSITION PICHE HOGA
# NOTICE KR -> SLOW POINTER USS NODE KO POINT KR RHA HAI JISE TUJHE DELETE KRNA HAI
# SLOW AND FAST MOVE WITH SAME SPEED
# YEHI TRICK THI QUESTION KI
# --------------------------------------------

# Optimal approach: Two‑pointer technique (one pass)
# Idea:

# Use two pointers: fast and slow
# Move fast pointer n steps ahead
# Then move fast and slow together until fast reaches the end
# Now slow is just before the node you need to delete
# Delete slow.next

# This works in one pass (O(n)).

    

