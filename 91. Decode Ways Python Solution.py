class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0" or s=='':
            return 0
        ctr=[0 for i in range(len(s)+1)]
        ctr[0]=1
        ctr[1]=1
        for i in range(2,len(s)+1):
            if s[i-1]>'0':
                ctr[i]=ctr[i-1] 
            if s[i-2]=='1' or s[i-2]=='2' and s[i-1]<'7':
                ctr[i]+=ctr[i-2] 
        return ctr[-1]