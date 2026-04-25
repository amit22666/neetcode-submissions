# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcdVal = math.gcd(prev.val, cur.val)

            gcdNode = ListNode(gcdVal)

            prev.next = gcdNode
            gcdNode.next = cur
            prev = cur
            cur = cur.next


        return head
