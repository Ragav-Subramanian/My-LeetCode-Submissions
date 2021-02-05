class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.replace("//","/").rstrip("/").split("/")
        print(path)
        stack=[]
        for i in path:
            if not i:
                continue
            if i==".":
                pass
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        stack="/"+"/".join(stack)
        return stack