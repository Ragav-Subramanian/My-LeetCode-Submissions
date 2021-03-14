# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l=0
        temp=head 
        while temp:
            temp=temp.next
            l+=1 
        if l<k or 2*k-1==l:
            return head
        firstnext = head 
        first = None 
        for i in range(k - 1): 
            first = firstnext 
            firstnext = firstnext.next
        secondnext = head 
        second = None 
        for i in range(l - k): 
            second = secondnext 
            secondnext = secondnext.next
        if first is not None: 
            first.next = secondnext
        if second is not None: 
            second.next = firstnext
        firstnext.next,secondnext.next = secondnext.next,firstnext.next 
        if k == 1: 
            head = secondnext   
        if k == l: 
            head = firstnext
        return head