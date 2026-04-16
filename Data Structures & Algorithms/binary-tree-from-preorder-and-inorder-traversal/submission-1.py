# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # i'm thinking in right direction?
        # i will iterate preorder array
        # ith node will be root. create the node
        # find ith node in inoder array
        # all the nodes left to ith node will be left subtree
        # all the nodes right to the ith node will right subtree

        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        
        # Map value -> index in inorder for O(1) lookup
        index = {val:i for i, val in enumerate(inorder)}
        self.pre_index = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index = self.pre_index + 1
            root = TreeNode(root_val)

            inorder_root_idx = index[root_val]

            root.left = build(in_left,inorder_root_idx-1)
            root.right = build(inorder_root_idx+1, in_right)
            return root
        return build(0,len(inorder)-1)

        