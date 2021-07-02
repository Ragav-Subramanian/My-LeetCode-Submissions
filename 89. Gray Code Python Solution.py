class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[0]
        isp=set()
        isp.add(0)
        def helper(n):
            if len(ans)==1<<n:
                return True
            cur = ans[-1]
            for i in range(n):
                next = cur^1<<i
                if next not in isp:
                    isp.add(next)
                    ans.append(next)
                    if helper(n):
                        return True
                    isp.discard(next)
                    ans.pop()
            return False
        helper(n)
        return ans