# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        if head.val==head.next.val and head.next.next is None:
            return head
        temp=ListNode(head.val)
        head=head.next 
        while head:
            if head and head.val<=temp.val:
                temp=ListNode(head.val,temp)
                head=head.next
                continue
            t=temp
            prev=temp
            while t and head.val>t.val:
                prev=t
                t=t.next 
            prev.next=ListNode(head.val,t)
            head=head.next
        return temp