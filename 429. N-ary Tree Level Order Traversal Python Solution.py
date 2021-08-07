"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        bfs=[root]
        while bfs:
            t=[]
            temp=[]
            for i in bfs:
                temp.append(i.val)
                for j in i.children:
                    if j:
                        t.append(j)
            ans.append(temp)
            bfs=t[:]
        return ans