# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Variable to track if the tree is balanced
        istreeBal = True

        def height(node: Optional[TreeNode]) -> int:
            nonlocal istreeBal
            if not node:
                return 0
            
            lht = height(node.left)
            rht = height(node.right)

            if abs(lht - rht) > 1:
                istreeBal = False

            return max(lht, rht) + 1

        # Compute height and check balance
        height(root)
        return istreeBal
