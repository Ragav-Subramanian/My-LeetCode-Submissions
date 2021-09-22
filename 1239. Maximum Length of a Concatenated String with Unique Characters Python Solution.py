class Solution:
    def maxLength(self, arr: List[str]) -> int:     
        return self.dfs(arr, 0, "")
    
    def dfs(self, arr, pos, res):
        if len(res) != len(set(res)):
            return 0

        # Recurse through each possible next option
        # and find the best answer
        best = len(res)
        for i in range(pos, len(arr)):
            best = max(best, self.dfs(arr, i + 1, res + arr[i]))
        return best