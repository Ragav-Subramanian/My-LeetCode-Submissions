class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l=[False for i in range(len(rooms))]
        def dfs(i):
            if l[i]:
                return
            l[i]=True
            for j in rooms[i]:
                dfs(j)
        dfs(0)
        return all(l)