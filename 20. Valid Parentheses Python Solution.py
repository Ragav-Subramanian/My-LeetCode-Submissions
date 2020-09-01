class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return True
        if len(s)<2:
            return False
        l=[]
        ob="[{("
        for i in s:
            if i in ob:
                l.append(i)
            if i not in ob:
                try:
                    p=l.pop()
                    if i==']' and p=='[':
                        continue
                    if i=='}' and p=='{':
                        continue
                    if i==')' and p=='(':
                        continue
                    return False
                except:
                    return False
        if l==[]:
            return True
        return False
        