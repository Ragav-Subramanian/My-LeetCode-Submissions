class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans=0
        ctr = [Counter(i) for i in strs]
        @lru_cache(None)
        def recurse(i,o,z,m,n):
            if i>=len(strs) or (o==n and z==m):
                return 0 
            t=0
            if ctr[i]['1']+o<=n and ctr[i]['0']+z<=m:
                t=1+recurse(i+1,ctr[i]['1']+o,ctr[i]['0']+z,m,n)
            return max(t,recurse(i+1,o,z,m,n))
        return recurse(0,0,0,m,n)