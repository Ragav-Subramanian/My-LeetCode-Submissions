class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)] 
        for i in range(m - 1): 
            for j in range(1, n): 
                dp[j] += dp[j - 1] 
        return dp[n - 1] 