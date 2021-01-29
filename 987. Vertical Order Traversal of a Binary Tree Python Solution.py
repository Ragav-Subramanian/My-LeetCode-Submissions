# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d={}
        def helper(root,x,y):
            if root:
                if x in d:
                    d[x][y]=d[x].get(y,[])+[root.val]
                else:
                    d[x]={}
                    d[x][y]=[root.val]
                if root.left:
                    helper(root.left,x-1,y-1)
                if root.right:
                    helper(root.right,x+1,y-1)
        helper(root,0,0)
        ans=[]
        for i in sorted(d):
            t=[]
            for j in sorted(d[i],reverse=True):
                t.extend(sorted(d[i][j]))
            ans.append(t)
        return ans