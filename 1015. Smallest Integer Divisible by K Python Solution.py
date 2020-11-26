class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0:
            return -1
        rem = 0
        for i in range(K):
            rem = (rem*10+1)%K 
            if rem==0:
                return i+1 
        return -1