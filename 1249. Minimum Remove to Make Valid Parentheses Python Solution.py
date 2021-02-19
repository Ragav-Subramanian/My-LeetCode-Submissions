class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans=list(s)
        stack=[]
        for i,j in enumerate(s):
            if j=='(':
                stack.append(i)
            elif j==')':
                if len(stack)>0:
                    stack.pop()
                else:
                    ans[i]=""
        for i in stack:
            ans[i]=""
        return "".join(ans)