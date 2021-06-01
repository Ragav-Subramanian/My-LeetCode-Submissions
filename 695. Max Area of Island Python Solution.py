class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        s=set()
        def helper(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 0 
            grid[i][j]=0
            return 1 + helper(i+1,j) + helper(i,j+1) + helper(i-1,j) + helper(i,j-1)
        ctr=0
        for i in range(r):
            for j in range(c):
                ctr=max(ctr,helper(i,j))
        return ctr