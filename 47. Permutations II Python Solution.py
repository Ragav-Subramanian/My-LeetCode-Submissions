from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=[]
        for i in permutations(nums):
            if list(i) not in l:
                l.append(list(i))
        return l