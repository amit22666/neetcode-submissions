# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # left, root, right
        # inorder traversal gives array in sorted order
        res = None

        def inorder(root):
            nonlocal k, res
            if not root or res is not None:
                return
            inorder(root.left)
            k = k - 1
            if k == 0:
                res = root.val
                return # we found the answer, early exit
            inorder(root.right)
            
        inorder(root)
        # if k was valid , res must be set
        return res
