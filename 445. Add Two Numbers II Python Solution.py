# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=0
        num2=0
        while l1:
            num1=num1*10+l1.val 
            l1=l1.next 
        while l2:
            num2=num2*10+l2.val 
            l2=l2.next 
        num3=num1+num2 
        if num3==0:
            return ListNode(0)
        ans=None
        while num3>0:
            node=ListNode(num3%10,ans)
            ans=node
            num3//=10
        return ans