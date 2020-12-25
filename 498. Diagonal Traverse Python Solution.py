class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        r,c=len(matrix),len(matrix[0])
        matrix=[i[::-1] for i in matrix[::-1]]
        ans=[[] for i in range(r+c-1)]
        for i in range(r):
            for j in range(c):
                ans[i+j]+=[matrix[i][j]]
        sol=[]
        for i,j in enumerate(ans[::-1]):
            if i%2:
                sol.extend(j[::-1])
            else:
                sol.extend(j)
        return sol