class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        ind=[]
        for i,j in enumerate(s):
            if j==c:
                ind.append(i)
        for i in range(len(s)):
            m=len(s)
            for j in ind:
                m=min(m,abs(j-i))
            ans.append(m)
        return ans