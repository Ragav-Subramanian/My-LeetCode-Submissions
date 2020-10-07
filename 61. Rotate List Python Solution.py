# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        if head.next==None:
            return head
        if k==0:
            return head
        temp=ListNode(head.val,head.next)
        t=0
        while temp!=None:
            temp=temp.next
            t+=1
        if k==t or k%t==0:
            return head 
        k=k%t 
        temp=ListNode(head.val,head.next)
        for i in range(t):
            if i==t-k:
                break 
            temp=temp.next
        tail=temp
        while temp.next!=None:
            temp=temp.next 
        temp.next=head
        while head.next!=tail:
            head=head.next
        head.next=None
        return tail