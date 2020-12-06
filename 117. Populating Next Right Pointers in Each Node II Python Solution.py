"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        bfs=[root]
        while bfs:
            t=[]
            l=len(bfs)
            for val in range(l-1):
                if bfs[val]:
                    if bfs[val].left:
                        t.append(bfs[val].left)
                    if bfs[val].right:
                        t.append(bfs[val].right)
                    bfs[val].next=bfs[val+1]
            if bfs[-1]:
                if bfs[-1].left:
                    t.append(bfs[-1].left)
                if bfs[-1].right:
                    t.append(bfs[-1].right)
            bfs=t[:]
        return root