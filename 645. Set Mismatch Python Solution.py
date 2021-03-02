class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        dup,mis=None,None
        for i in range(1,len(nums)+1):
            if i in d:
                if d[i]==2:
                    dup=i
            else:
                mis=i
        return dup,mis