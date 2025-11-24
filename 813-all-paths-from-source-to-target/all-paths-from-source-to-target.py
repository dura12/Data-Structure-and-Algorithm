class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        ans = []
        
        def dfs(node, path):
            # Base Case: If we reached the destination node
            if node == end:
                ans.append(list(path)) # Make a copy of the path and add to answers
                return 
            
            # Recursive Step
            for nei in graph[node]:
                # Proceed to neighbors
                path.append(nei)
                dfs(nei, path)
                path.pop() # Backtrack: Remove the neighbor to try the next one
        
        # Start DFS from node 0, with [0] as the initial path
        dfs(0, [0])
        return ans