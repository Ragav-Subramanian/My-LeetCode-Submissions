class Solution(object):
    def longestMountain(self, A):
        N = len(A)
        ans, start = 0, 0
        while start < N:
            end = start
            if end + 1 < N and A[end] < A[end + 1]: 
                while end+1 < N and A[end] < A[end+1]:
                    end += 1
                if end + 1 < N and A[end] > A[end + 1]: 
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    ans = max(ans, end - start + 1)
            start = max(end, start + 1)
        return ans