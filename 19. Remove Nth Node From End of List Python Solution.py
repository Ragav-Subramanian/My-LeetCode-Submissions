# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        temp=head
        c=0
        while temp!=None:
            c+=1 
            temp=temp.next
        prev=head
        if c==n:
            head=head.next
            return head
        c-=n
        temp=head
        while c>0:
            c-=1 
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return head