class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ec = 0
        oc = 0
        for i in position:
            if i % 2 == 0:
                ec += 1
            else:
                oc += 1
        return min(ec, oc)