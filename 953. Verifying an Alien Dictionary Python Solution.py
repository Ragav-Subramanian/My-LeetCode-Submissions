class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        prev=words[0]
        for word in words[1:]:
            if len(prev)!=len(word):
                prev=prev.ljust(max(len(prev),len(word)))
                word=word.ljust(max(len(prev),len(word)))
            for a,b in zip(prev,word):
                if a!=b:
                    break
            ai,bi=order.find(a),order.find(b)
            if ai>bi:
                return False 
            prev=word
        return True