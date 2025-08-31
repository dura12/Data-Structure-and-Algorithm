class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def inbound(row , col):
            return 0<= row < m and 0<= col < n
        def dfs(row , col):
            if (row , col) in cache:
                return cache[row,col]
            if row == m - 1 and col == n - 1:
                return 1
            if not inbound(row , col):
                return 0
            ans = 0
            ans += dfs(row + 1 , col)
            ans += dfs(row , col + 1)
            cache[row,col] = ans
            return cache[row,col] 
        return dfs(0,0)