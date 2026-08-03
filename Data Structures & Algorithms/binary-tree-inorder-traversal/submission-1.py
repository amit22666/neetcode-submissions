# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root

        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right   # putting cur to right position
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right  # putting prev to right position

                if not prev.right: # linking
                    prev.right = cur # linking
                    cur = cur.left
                else:
                    prev.right = None  # de-linking
                    res.append(cur.val)
                    cur = cur.right

        return res