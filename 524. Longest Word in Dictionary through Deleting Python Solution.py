class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda i:(-len(i),i))
        for i in d:
            ind=0
            for j in s:
                if ind<len(i) and i[ind]==j:
                    ind+=1 
            if ind==len(i):
                return i
        return ""