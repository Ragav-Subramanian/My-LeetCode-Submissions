class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l=list(range(1,10))
        a=[]
        for i in combinations(l,k):
            if sum(i)==n:
                a.append(i)
        return a