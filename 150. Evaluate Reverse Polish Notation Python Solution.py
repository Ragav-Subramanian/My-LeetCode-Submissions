class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        o='/*+-'
        for i in tokens:
            if not i in o:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                stack.append(self.op(b,a,i))
        return stack[-1]
    def op(self,a,b,ch):
        if ch=='+':
            return a+b 
        if ch=='-':
            return a-b 
        if ch=='*':
            return a*b 
        if ch=='/':
            return int(a/b)