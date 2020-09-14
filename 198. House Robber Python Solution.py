class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        a,b=0,0
        for i in nums:
            a,b=max(b+i,a),a
        return max(a,b)