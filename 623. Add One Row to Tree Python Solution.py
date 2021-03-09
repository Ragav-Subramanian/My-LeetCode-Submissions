# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        headroot = root
        if d==1:
            return TreeNode(v,root)
        bfs=[root]
        while d>2:
            d-=1
            t=[]
            for i in bfs:
                if i:
                    if i.left:
                        t.append(i.left)
                    if i.right:
                        t.append(i.right)
            bfs=t[:]
        for i in bfs:
            i.left=TreeNode(v,i.left)
            i.right=TreeNode(v,None,i.right)
        return headroot