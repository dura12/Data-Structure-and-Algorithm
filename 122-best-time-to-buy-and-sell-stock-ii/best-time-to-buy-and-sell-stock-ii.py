class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i , turn ):
            if i >= len(prices):
                return 0
            ans = 0
            if turn:
                ans += dfs(i + 1 , 0) - prices[i]
                without = dfs(i + 1 , 1) 
                return max(ans , without)
            else:
                ans += dfs(i + 1 , 1) + prices[i]
                withh = dfs(i + 1 , 0) 
                return max(ans , withh)

        return dfs(0,1)
                

