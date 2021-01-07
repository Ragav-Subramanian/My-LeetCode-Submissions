class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml=0
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
            ml=max(len(seen),ml)
        return ml