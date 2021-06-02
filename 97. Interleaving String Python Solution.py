class Solution:
    def isInterleave(self, a: str, b: str, c: str) -> bool:
        if len(a)+len(b)!=len(c):
            return False
        if not a and not b and not c:
            return True
        @lru_cache(None)
        def recurse(i,j,k):
            if i==len(a) and j==len(b) and k==len(c):
                return True
            if k==len(c):
                return False
            if i<len(a) and j<len(b):
                if a[i]==c[k] and b[j]==c[k]:
                    return recurse(i+1,j,k+1) or recurse(i,j+1,k+1)
            if i<len(a):
                if a[i]==c[k]:
                    return recurse(i+1,j,k+1)
            if j<len(b):
                if b[j]==c[k]:
                    return recurse(i,j+1,k+1)
        return recurse(0,0,0)