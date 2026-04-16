# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxdiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.maxdiameter

    def height(self, root: Optional[TreeNode]):

            if not root:
                return 0

            lh = self.height(root.left)
            rh = self.height(root.right)
            
            self.maxdiameter = max(self.maxdiameter, lh+rh)

            return max(lh,rh) +1 
        