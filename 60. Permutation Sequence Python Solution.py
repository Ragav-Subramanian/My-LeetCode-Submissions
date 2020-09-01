from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        for i in permutations(list(map(str,list(range(1,n+1))))):
            k-=1 
            if k==0:
                return "".join(i)