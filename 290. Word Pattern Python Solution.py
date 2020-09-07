class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d1={}
        d2={}
        k=0
        if len(pattern)!=str.count(' ')+1:
            return False
        for i in str.split():
            if i not in d1:
                d1[i]=pattern[k]
            else:
                if d1[i]!=pattern[k]:
                    return False
            if pattern[k] not in d2:
                d2[pattern[k]]=i 
            else:
                if d2[pattern[k]]!=i:
                    return False
            k+=1
        return True