class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        l=len(A)
        countA=[0 for i in range(7)]
        countB=[0 for i in range(7)]
        same=[0 for i in range(7)]
        for i in range(l):
            countA[A[i]]+=1
            countB[B[i]]+=1
            if (A[i] == B[i]):
                same[A[i]]+=1
        for i in range(1,7):
            if (countA[i] + countB[i] - same[i] == l):
                return l - max(countA[i], countB[i])
        return -1