# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxdiameter = 0

        def height(root: Optional[TreeNode]):

            if not root:
                return 0

            lh = height(root.left)
            rh = height(root.right)
            
            self.maxdiameter = max(self.maxdiameter, lh+rh)

            return max(lh,rh) +1 

        height(root)
        return self.maxdiameter
        