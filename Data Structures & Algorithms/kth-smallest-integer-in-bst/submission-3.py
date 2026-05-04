# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # left, root, right
        # inorder traversal gives array in sorted order
        
        # we will now do this via morris traversal
        # left subtree ki last node (leaf hogi) (right node) -> usko connect kr denge root se
        # iss se hame extra space nhi chahiye hoga (stack,recursive stack)
        # wapis jane ke lie temporary "thread" banate hai "predecessor.right = cur"

        curr = root

        while curr:
            if curr.left is None:
                k = k - 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                # find inorder predecessor: left subtree ka rightmost node

                pred = curr.left
                while pred.right and pred.right is not curr: 
                    # pred.right is not curr -> connection is not set
                    pred = pred.right

                if pred.right is None:
                    # node jiska right none hai <- found that node
                    # Thead set karo: predecessor.right = curr
                    # Taaki left subtree traverse karke wapas curr pr aa sake
                    pred.right = curr # <-- MAIN LOGIC
                    curr = curr.left
                else:
                    # THread already tha -> remove karo (restore tree)
                    pred.right = None
                    # ab curr ko visit karo (left done, thread removed)
                    k = k - 1
                    if k == 0:
                        return curr.val
                    # move to right
                    curr = curr.right
