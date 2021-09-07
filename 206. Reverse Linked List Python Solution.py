# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        ans=ListNode(head.val)
        prev=None 
        while head.next is not None:
            prev=head.next 
            newNode = ListNode(prev.val,ans)
            ans=newNode 
            head=head.next
        return newNode