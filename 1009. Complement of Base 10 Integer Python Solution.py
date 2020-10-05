class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N=bin(N)[2:]
        b=""
        for i in N:
            if i=='1':
                b+='0' 
            else:
                b+='1'
        return int(b,2)