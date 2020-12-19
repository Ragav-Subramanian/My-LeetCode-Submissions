class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return -inf
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            if row != m-1:
                result += max(dp(row+1,col1,col2),dp(row+1,col1-1,col2-1),dp(row+1,col1-1,col2),dp(row+1,col1,col2-1),dp(row+1,col1+1,col2-1),dp(row+1,col1-1,col2+1),dp(row+1,col1+1,col2+1),dp(row+1,col1,col2+1),dp(row+1,col1+1,col2))
            return result
        return dp(0, 0, n-1)