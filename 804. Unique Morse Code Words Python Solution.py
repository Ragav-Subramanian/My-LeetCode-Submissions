class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d=dict(zip([chr(i) for i in range(97,123)],[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
))
        s=set()
        for i in words:
            k=''
            for j in i:
                k+=d[j]
            s.add(k)
        return len(s)