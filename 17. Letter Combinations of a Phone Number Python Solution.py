class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans=[]
        def dfs(ind,t):
            if ind==len(digits):
                ans.append(t)
                return 
            for i in d[digits[ind]]:
                dfs(ind+1,t+i)
        dfs(0,'')
        return ans