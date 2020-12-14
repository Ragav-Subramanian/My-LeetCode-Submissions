class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans=[]
        self.dfs(s,[])
        return self.ans
    def dfs(self,s,temp):
        if not s:
            self.ans.append(temp)
        for i in range(1,len(s)+1):
            if self.isp(s[:i]):
                self.dfs(s[i:],temp+[s[:i]])
    @lru_cache(None)
    def isp(self,s):
        l=len(s)-1
        i=0
        while i<l:
            if s[i]!=s[l]:
                return False
            i+=1
            l-=1
        return True