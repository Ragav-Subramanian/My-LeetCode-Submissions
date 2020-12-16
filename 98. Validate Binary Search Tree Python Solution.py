# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.ans=[]
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
        helper(root)
        for i in range(1,len(self.ans)):
            if self.ans[i]<=self.ans[i-1]:
                return False
        return True
    