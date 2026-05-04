# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at each node we have a choice -> rob or not rob 

        # [pick/rob root, not pick/rob root]

        def dfs(root): # return list of 2 value
            if not root:
                return [0,0]

            # left
            leftResult = dfs(root.left)
            # right
            rightResult = dfs(root.right)

            # choice diagram
            # leftResult[0] -> pick
            # leftResult[1] -> pick nhi kia

            # root pick
            withRoot =  root.val + leftResult[1] + rightResult[1]

            # root pick nhi kra
            withoutRoot = max(leftResult) + max(rightResult)

            return [withRoot, withoutRoot]
        
        result = dfs(root) 
        return max(result) # result will have 2 value pick root, not pick root