# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.istreeBal = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Compute height and check balance
        self.height(root)
        return self.istreeBal

    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        lht = self.height(node.left)
        rht = self.height(node.right)

        if abs(lht - rht) > 1:
            self.istreeBal = False

        return max(lht, rht) + 1
