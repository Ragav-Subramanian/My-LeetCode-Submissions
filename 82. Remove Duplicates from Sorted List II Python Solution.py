# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d={}
        while head:
            d[head.val]=d.get(head.val,0)+1 
            head=head.next
        head=None
        tail=None
        for i in d:
            if d[i]==1:
                if not head:
                    head=ListNode(i)
                    tail=head
                else:
                    node=ListNode(i)
                    tail.next=node 
                    tail=tail.next
        return head