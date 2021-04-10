class Solution:
    def longestIncreasingPath(self, l: List[List[int]]) -> int:
        @cache
        def dfs(i,j):
            val=l[i][j]
            return 1+max(dfs(i+1,j) if i+1<len(l) and val<l[i+1][j] else 0,
                         dfs(i,j+1) if j+1<len(l[0]) and val<l[i][j+1] else 0,
                         dfs(i-1,j) if i>0 and val<l[i-1][j] else 0,
                         dfs(i,j-1) if j>0 and val<l[i][j-1] else 0)
        return max(dfs(i,j) for i in range(len(l)) for j in range(len(l[0])))