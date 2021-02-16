class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        s=list(s)
        def permute(i):
            if i==len(s):
                ans.append("".join(s))
                return
            if s[i].isdigit():
                permute(i+1)
                return
            s[i]=s[i].lower()
            permute(i+1)
            s[i]=s[i].upper()
            permute(i+1)
        permute(0)
        return ans