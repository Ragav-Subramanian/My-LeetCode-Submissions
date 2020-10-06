# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:
            root=TreeNode(val)
            return root
        if root.val>val:
            if root.left is None:
                root.left=TreeNode(val)
            else:
                root.left=self.insertIntoBST(root.left,val)
        else:
            if root.right is None:
                root.right=TreeNode(val)
            else:
                root.right=self.insertIntoBST(root.right,val)
        return root