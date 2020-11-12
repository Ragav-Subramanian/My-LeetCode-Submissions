class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s=set()
        for i in permutations(nums):
            s.add(i)
        return list(s)