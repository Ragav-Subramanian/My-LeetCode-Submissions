class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        val=[0 for i in range(101)]
        val[1]=1
        for i in range(1,n+1):
            v1=2*i 
            v2=2*i+1
            if v1<=n:
                val[v1]=val[i]
            if v2<=n:
                val[v2]=val[i]+val[i+1]
        return max(val)