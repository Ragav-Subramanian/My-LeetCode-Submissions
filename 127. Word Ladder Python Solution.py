class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s=set(wordList)
        d={beginWord:0}
        seen=set()
        ans=[]
        while d:
            flag=True
            temp={}
            for word in d:
                if word==endWord:
                    ans.append(d[word])
                if word not in seen:
                    d[word]+=1 
                    seen.add(word)
                    for i in range(len(word)):
                        for c in map(chr,range(97,97+26)):
                            v=word[:i]+c+word[i+1:]
                            if v not in seen and v in s:
                                temp[v]=d[word]
                                flag=False
            d=temp
            if flag:
                break
        if ans:
            return min(ans)+1
        return 0