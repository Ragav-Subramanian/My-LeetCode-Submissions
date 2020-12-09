class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c=0
        d={}
        for i in time:
            if i%60==0:
                c+=d.get(i%60,0)
            else:
                c+=d.get(60-i%60,0)
            d[i%60] = d.get(i%60,0)+1
        return c