class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        def inbound(row , col):
            return 0<= row < m and 0<= col < n
        def dfs(row , col):
            if (row , col) in cache:
                return cache[row,col]
            if row == m - 1 and col == n - 1:
                return 1
            if not inbound(row , col):
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            ans = 0
            ans += dfs(row + 1 , col)
            ans += dfs(row , col + 1)
            cache[row,col] = ans
            return cache[row,col] 
        return dfs(0,0)