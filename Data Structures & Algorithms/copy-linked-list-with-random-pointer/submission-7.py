"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None # missed this
        mapping_old_to_new = {}
        cur = head
        while cur:
            new_node = Node(cur.val,None,None)
            mapping_old_to_new[cur] = new_node
            cur = cur.next
        cur = head
        # Now we will connecting links
        # next and random
        while cur:
            new_node = mapping_old_to_new[cur]
            # .get -> i missed this
            new_node.random = mapping_old_to_new.get(cur.random)
            new_node.next = mapping_old_to_new.get(cur.next)
            cur = cur.next
        return mapping_old_to_new[head]
        

            


        # this is order of (n) space complexity
        # Pass 1 — Clone all nodes + build the next links
            # Iterate through the original list.
            # For each original node, create a new deep-copied node.
            # Store the mapping:
            # old_node → new_node
            # Also, connect the next pointers for the new list during this pass.

            #  After pass 1, you will have:

            # All new nodes created.
            # next pointers correctly connected.
            # A hashmap that lets you quickly look up cloned nodes.
        # Pass 2 — Fix the random pointers
            # Iterate through the original list again.
            # For each node:

            # Look at old_node.random
            # Use the map to get the corresponding new random pointer:
            # new_node.random = map[old_node.random]

            
        