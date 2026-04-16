# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        # we have to merge k list
        # we will use linked list
        # we will take two list and merge them
        # after that store it in result
        # return result [0]

        # Merge two list
        # we will have temp node infront so that we can return the answer
        # we will maintain tail pointer
        # we will add new node to tail.next pointer
        # we will move tail to next position. so that it comes at end


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None
        
        merged = None

        # Merge lists one-by-one
        for lst in lists:
            merged = self.mergeTwoList(merged,lst)
        return merged

    def mergeTwoList(self, node1, node2):
        temp = ListNode()
        tail = temp

        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        # FIXED: attach the remaining nodes
        if node1:
            tail.next = node1
        elif node2:
            tail.next = node2

        return temp.next

        