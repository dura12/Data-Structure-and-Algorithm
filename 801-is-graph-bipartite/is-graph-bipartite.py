class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
        visit = set()
        def dfs(node):
            for nei in graph[node]:
                if color[nei] == 0:
                    color[nei] = -color[node]
                    if not dfs(nei):
                        return False
                elif color[nei] != 0 and color[nei] == color[node]:
                    return False
                else:
                    color[nei] = -color[node]  
            return True
        for i in range(len(graph)):
            if color[i] == 0:
                color[i] = 1
                if not dfs(i):
                    return False
        return True
        return dfs(0) 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
