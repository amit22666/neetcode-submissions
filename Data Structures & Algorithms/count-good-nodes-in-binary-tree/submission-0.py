# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxTillNow):
            if not node:
                return 0
            if node.val >= maxTillNow:
                res = 1
            else:
                res=0
            maxTillNow = max(maxTillNow,node.val)
            res += dfs(node.left,maxTillNow)
            res += dfs(node.right, maxTillNow)
            return res

        return dfs(root, root.val)

        