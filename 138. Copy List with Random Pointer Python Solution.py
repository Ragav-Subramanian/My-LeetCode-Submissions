"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
Solution 1:
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return deepcopy(head)

Solution 2:

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        temp=head
        mp = {}
        t=head
        while temp:
            mp[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.next:
                mp[temp].next=mp[temp.next]
            if temp.random:
                mp[temp].random=mp[temp.random]
            temp=temp.next
        return mp[head]