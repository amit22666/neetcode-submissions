# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # res stores the maximum path sum seen so far
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # compute max path sum from left and right subtree
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            # ignore negative paths
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)

            # choice 1: path passing through current node
            currentPath = node.val + leftSum + rightSum
            res[0] = max(res[0], currentPath)

            # choice 2: return path upward (only one side allowed)
            return node.val + max(leftSum, rightSum)

        dfs(root)
        return res[0]
