# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans=[]
        bfs=[root]
        while bfs:
            ans.append(bfs[-1].val)
            t=[]
            l=len(bfs)
            for i in range(l):
                if bfs[i]:
                    if bfs[i].left:
                        t.append(bfs[i].left)
                    if bfs[i].right:
                        t.append(bfs[i].right)
            bfs=t[:]
        return ans