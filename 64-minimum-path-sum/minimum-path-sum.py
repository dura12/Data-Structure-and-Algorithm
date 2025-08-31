class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        m = len(grid)
        n = len(grid[0])
        def inbound(row , col):
            return 0<= row < m and 0<= col < n
        def dfs(row , col):
            if (row , col) in cache:
                return cache[row,col]
            if not inbound(row , col):
                return float("inf")
            if row == m - 1 and col == n - 1:
                return grid[m-1][n-1]
            ans = 0
            ans += min(grid[row][col] + dfs(row + 1 , col),
            grid[row][col] + dfs(row , col + 1))
            cache[row,col] = ans
            return cache[row,col] 
        return dfs(0,0)