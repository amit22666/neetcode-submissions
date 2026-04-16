# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # I THOUGHT THIS BUT THIS IS WORNG
        # please tell if i'm thinking in the right direction or not
        # i will take two dummy node/pointer . Put at front and at rear
        # after that take the rear element attach in between 0th and 1st element
        # then move the first pointer by 2 so that we come to second element from front
        # then attach the last element to this and next node
        

        # WHAT WE HAVE TO DO HERE IS
        # FIND THE MIDDLE -> SLOW AND FAST
        # REVERSE THE SECOND HALF
        # MERGE THE TWO HALVES ALTERNATIVELY
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        MiddleKaNext = slow.next

        # cut the refrence

        prev = None
        slow.next = None

        while MiddleKaNext:
            temp = MiddleKaNext.next
            MiddleKaNext.next = prev
            prev = MiddleKaNext
            MiddleKaNext = temp

        first = head
        # reversed list ka head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

