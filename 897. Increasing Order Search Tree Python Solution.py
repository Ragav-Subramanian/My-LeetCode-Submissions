# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans=TreeNode()
        temp=self.ans
        def helper(root):
            if root is None:
                return
            helper(root.left)
            self.ans.right=TreeNode(root.val)
            self.ans=self.ans.right
            helper(root.right)
        helper(root)
        return temp.right