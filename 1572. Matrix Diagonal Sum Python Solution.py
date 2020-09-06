class Solution:
    def diagonalSum(self, l: List[List[int]]) -> int:
        md=0 
        od=0 
        for i in range(len(l)): 
            for j in range(len(l)): 
                if i==j: 
                    md+=l[i][j] 
                elif i+j==len(l)-1: 
                    od+=l[i][j] 
        return md+od