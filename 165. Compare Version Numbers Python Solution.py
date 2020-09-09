class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        while v1 or v2:
            val1 = v1.pop(0) if v1 else 0
            val2 = v2.pop(0) if v2 else 0
            if val1 > val2: return 1
            elif val1 < val2: return -1
        return 0