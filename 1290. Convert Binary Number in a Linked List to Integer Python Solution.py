# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b=""
        while head!=None:
            b+=str(head.val)
            head=head.next
        return int(b,2)1290. Convert Binary Number in a Linked List to Integer
