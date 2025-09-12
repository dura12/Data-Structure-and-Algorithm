class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = 0
        n = len(triangle)
        m = len(triangle[0])
        @cache
        def dfs(row , col):
            if row == n - 1:
                return triangle[row][col]
            sum1 = 0
            sum1 += (min( dfs(row + 1 ,col),dfs(row + 1 , col+1))
            + triangle[row][col]  )
            return sum1
        return dfs(0,0)