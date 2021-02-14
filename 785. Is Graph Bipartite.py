class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        def dfs(clr,node):
            if node in color:
                return color[node]==clr
            color[node]=clr
            for i in graph[node]:
                if not dfs(-clr,i):
                    return False
            return True
        for i in range(len(graph)):
            if i not in color and not dfs(1,i):
                return False
        return True