class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=len(s)
        if l<10:
            return []
        d={}
        val=s[:10]
        d[val]=1
        v=0
        for i in range(10,l):
            val=val[1:]+s[i]
            d[val]=d.get(val,0)+1
        ans=[]
        for i in d:
            if d[i]>1:
                ans.append(i)
        return ans