# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # An empty tree is a subtree of any tree
            return True
        if not root:  # A non-empty tree cannot be a subtree of an empty tree
            return False

        # Check if the current trees are identical
        sameTreeAns = self.SameTree(root, subRoot)

        # Check the left and right subtrees
        lst = self.isSubtree(root.left, subRoot)
        rst = self.isSubtree(root.right, subRoot)

        return sameTreeAns or lst or rst

    def SameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:  # Both trees are empty
            return True
        if not root or not subRoot:  # One tree is empty
            return False

        # Check if current nodes and their subtrees are identical
        if root.val != subRoot.val:
            return False

        lst = self.SameTree(root.left, subRoot.left)
        rst = self.SameTree(root.right, subRoot.right)

        return lst and rst
