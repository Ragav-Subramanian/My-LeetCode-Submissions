class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        c_s = lambda x : sum([ceil(i/x) for i in nums])
        left, right = 1, nums[-1]
        while left <= right:
            ind = (right + left) >> 1
            if c_s(ind) > threshold:
                left = ind + 1
            else:
                right = ind - 1
        return left