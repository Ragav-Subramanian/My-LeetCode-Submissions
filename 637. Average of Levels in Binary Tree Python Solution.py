# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        l=[root]
        ans=[]
        while l:
            t=[]
            a=[]
            for i in l:
                if i is not None:
                    if i.left is not None:
                        t.append(i.left)
                    if i.right is not None:
                        t.append(i.right)
                    a.append(i.val)
            ans.append(sum(a)/len(a))
            l=t[:]
        return ans