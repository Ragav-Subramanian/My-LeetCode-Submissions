#Refer my C Solution for Exact approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: 
            return 0 
        else:  
            a=str(x)
            if x==(int(a[::-1])): 
                return 1 
            else: 
                return 0