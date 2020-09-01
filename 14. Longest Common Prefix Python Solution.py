class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ""
        for i in range(len(strs[0]),0,-1):
            f = 0
            for j in range(1,len(strs)):
                if not strs[j].startswith(strs[0][:i]):
                    f = 1
                    break
            if f==0:
                return strs[0][:i]
        return ""
            