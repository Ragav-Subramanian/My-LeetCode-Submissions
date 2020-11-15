# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans=0
        def helper(root):
            if root:
                if root.val>=low and root.val<=high:
                    self.ans+=root.val 
                if low<root.val:
                    helper(root.left)
                if high>root.val:
                    helper(root.right)
        helper(root)
        return self.ans