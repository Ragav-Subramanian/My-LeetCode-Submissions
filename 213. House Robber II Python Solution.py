class Solution:
    def rob(self, nums: List[int]) -> int:
        def heist(nums: List[int]) -> int:
            if len(nums)==0:
                return 0
            a,b=0,0
            for i in nums:
                a,b=max(b+i,a),a
            return max(a,b)
        l=len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        if l<=3:
            return max(nums)
        return max(heist(nums[1:]),heist(nums[:-1]))