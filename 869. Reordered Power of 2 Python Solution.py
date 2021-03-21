class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def permute(i,s,l):
            if i==l:
                if s[0]=='0':
                    return False
                t=int(''.join(s))
                return t&(t-1)==0
            for j in range(i,l):
                s[i],s[j]=s[j],s[i]
                if permute(i+1,s[:],l):
                    return True
                s[i],s[j]=s[j],s[i]
            return False
        return permute(0,list(str(N)),len(str(N)))