class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums=[]
        heapify(nums)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(nums,matrix[i][j])
        while k>1:
            heappop(nums)
            k-=1
        return heappop(nums)