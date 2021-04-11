# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        l=[root]
        s=0
        while l!=[]:
            t=[]
            s=0
            for i in l:
                if i is not None:
                    if i.left is not None:
                        t.append(i.left)
                    if i.right is not None:
                        t.append(i.right)
                    s+=i.val
            l=t[:]
        return s1