# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        if head.next == None:
            return False
        
        while head.next != None and head.next != 'visited':
            if head.val == 'visited':
                return True
            head.val = 'visited'
            head = head.next
        return False