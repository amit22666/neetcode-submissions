# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursion

        # stop condition / base condition
        if not root:
            return root

        #FORGOT TO PUT SELF
        # preorder left sub tree
        self.invertTree(root.left)

        # right sub tree
        self.invertTree(root.right)
        

        # logic
        # swap left substree, with right substree and visa versa
        root.left , root.right = root.right , root.left

        # FORGET TO RETURN ROOT
        return root

        

        
        