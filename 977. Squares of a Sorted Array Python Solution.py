class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i**2 for i in A])