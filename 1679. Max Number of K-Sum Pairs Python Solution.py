class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0
        d={}
        for i in nums:
            if k-i in d:
                c+=1
                d[k-i]-=1
                if d[k-i]==0:
                    del d[k-i]
            else:
                d[i]=d.get(i,0)+1
        return c