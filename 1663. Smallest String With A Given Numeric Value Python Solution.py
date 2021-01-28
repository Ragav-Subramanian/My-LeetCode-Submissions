class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans=['a']*n
        k-=n 
        while k>0:
            ans[n-1]=chr(ord(ans[n-1])+min(k,25))
            n-=1 
            k-=min(k,25)
        return "".join(ans)