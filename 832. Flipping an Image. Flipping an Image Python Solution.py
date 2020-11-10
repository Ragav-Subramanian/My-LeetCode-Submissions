class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]==0:
                    A[i][j]=1 
                else:
                    A[i][j]=0 
            A[i]=A[i][::-1]
        return A