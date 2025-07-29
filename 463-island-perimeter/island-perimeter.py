class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(row , col):
            return 0<=row<n and 0<=col<m 
        self.ans = 0
        visit = set()
        def dfs(row , col):
            if not inbound(row , col) or grid[row][col] == 0:
                return 1
            if (row,col) in visit:
                return 0
            ans = 0
            visit.add((row , col))
            for i , j in [(0,1),(1,0),(-1,0),(0,-1)]:
                new_r = i + row
                new_c = col + j
                ans += dfs(new_r , new_c)
            return ans
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return  dfs(i,j)
        return 0
            
