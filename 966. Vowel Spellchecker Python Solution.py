class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans=[]
        vows={}
        low={}
        normal={}
        for word in wordlist:
            normal[word]=0
            low[word.lower()]=low.get(word.lower(),[])+[word]
            t=""
            for i in word.lower():
                if i in "aeiou":
                    t+="*"
                else:
                    t+=i 
            vows[t]=vows.get(t,[])+[word]
        for query in queries:
            if query in normal:
                ans.append(query)
            elif query.lower() in low:
                ans.append(low[query.lower()][0])
            else:
                t=""
                for i in query.lower():
                    if i in "aeiou":
                        t+="*"
                    else:
                        t+=i 
                if t in vows:
                    ans.append(vows[t][0])
                else:
                    ans.append("")
        return ans