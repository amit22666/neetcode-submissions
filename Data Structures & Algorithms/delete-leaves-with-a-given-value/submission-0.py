# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        # left se delete
        # right se delete
        # phir root pr decision lia -> delete krna hai ya nhi

        # POST order traversal

        def dfs(root, target):
            
            if not root:
                return None
            
            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)

            if root.val == target and root.left == None and root.right == None:
                return None
            
            return root
        return dfs(root, target)
        