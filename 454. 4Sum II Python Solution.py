class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mp = {}
        for a in A:
            for b in B :
                if a + b in mp:
                    mp[a+b] += 1
                else :
                    mp[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in mp:
                    count += mp[-c-d]
        return count