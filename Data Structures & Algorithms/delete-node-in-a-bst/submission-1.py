
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def deleteNode(self, root: Optional['TreeNode'], key: int) -> Optional['TreeNode']:
        # BST mein deletion:
        # 1) key chhota ho to left subtree mein jao
        # 2) key bada ho to right subtree mein jao
        # 3) Mil jaaye to:
        #    - ek child missing ho to dusra child return karo
        #    - dono children hon to right subtree ka inorder successor (sabse chhota) lo,
        #      uska value current node mein daalo, aur successor ko delete kar do.

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found: delete cases
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Both children exist: find inorder successor (min in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Copy successor's value to current node
            root.val = successor.val
            # Delete the successor node from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root
