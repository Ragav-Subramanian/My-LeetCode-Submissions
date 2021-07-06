class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
            total_count += count
            if total_count >= len(arr) // 2:
                return index + 1
        return 0