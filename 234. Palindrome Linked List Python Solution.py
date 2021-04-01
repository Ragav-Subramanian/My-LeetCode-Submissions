# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp=head 
        k=[]
        while temp:
            k.append(temp.val)
            temp=temp.next
        if k==k[::-1]:
            return True
        return False