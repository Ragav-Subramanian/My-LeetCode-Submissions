class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0]*(rowIndex+1)
        ans[0] = 1
        s = 0
        for i in range(1,rowIndex+1):
            prev = 1
            for j in range(1,i):
                s = prev + ans[j]
                prev = ans[j] 
                ans[j] = s 
            ans[i] = 1
        return ans