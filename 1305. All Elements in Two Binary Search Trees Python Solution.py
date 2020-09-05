# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.l=[]
        self.recurse(root1)
        self.recurse(root2)
        return sorted(self.l)
    def recurse(self,root):
        if root is None:
            return
        self.l.append(root.val)
        self.recurse(root.left)
        self.recurse(root.right)
        