# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.val=0
        self.helper(root,str(root.val))
        return self.val
    def helper(self,root,s):
        if root:
            if root.left:
                self.helper(root.left,s+str(root.left.val))
            if root.right:
                self.helper(root.right,s+str(root.right.val))
            if root.left is None and root.right is None:
                self.val+=int(s,2)
        return 