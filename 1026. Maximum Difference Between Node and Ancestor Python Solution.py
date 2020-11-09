# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans, self.mi, self.ma=-1, float('inf'), float('-inf')
        bfs=[root]
        while bfs:
            t=[]
            for i in bfs:
                if i.left is not None:
                    t.append(i.left)
                if i.right is not None:
                    t.append(i.right)
                self.traverse(i)
                self.ans = max(self.ans,abs(self.ma-i.val),abs(i.val-self.mi))
                self.mi, self.ma = float('inf'), float('-inf')
            bfs=t[:]
        return self.ans
    def traverse(self,root):
        if root is None:
            return
        self.mi=min(root.val,self.mi)
        self.ma=max(root.val,self.ma)
        self.traverse(root.left)
        self.traverse(root.right)