# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ans=None
        d={}
        while headA:
            d[headA]=headA 
            headA=headA.next 
        while headB:
            if headB in d:
                return headB
            headB=headB.next
        return ans1