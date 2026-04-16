# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at every node we have to decide 
        # is left subtree bst?
        # is right subtree bst?
        # at root we need minvalue from left subree 
        # maxvalue from right subtree then check bst propertry

        def dfs(root):
            if not root:
                return True, float('inf'),float('-inf')

            left_ok, left_min, left_max =  dfs(root.left)
            right_ok, right_min, right_max = dfs(root.right)
            cur_ok = left_ok and right_ok and left_max < root.val < right_min 

            cur_min = min(left_min,root.val)
            cur_max = max(right_max, root.val)

            return cur_ok, cur_min, cur_max

        answer = dfs(root)
        return answer[0]
        