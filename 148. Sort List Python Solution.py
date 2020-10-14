# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        if head.val<head.next.val:
            ans=ListNode(head.val)
            tail=ListNode(head.next.val)
        else:
            ans=ListNode(head.next.val)
            tail=ListNode(head.val)
        ans.next=tail
        head=head.next.next
        while head is not None:
            if ans.val>=head.val:
                ans=ListNode(head.val,ans)
            elif tail.val<=head.val:
                tail.next=ListNode(head.val)
                tail=tail.next
            else:
                temp=ans
                while temp.next.val<head.val:
                    temp=temp.next 
                temp.next=ListNode(head.val,temp.next)
            head=head.next
        return ans