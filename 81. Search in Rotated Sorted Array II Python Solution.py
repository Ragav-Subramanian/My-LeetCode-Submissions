class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            v=nums.index(target) 
            return True
        except:
            return False