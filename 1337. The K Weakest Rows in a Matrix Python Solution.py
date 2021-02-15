class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[1] for i in sorted([(sum(j),i) for i,j in enumerate(mat)])[:k]]