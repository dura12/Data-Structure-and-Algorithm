class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(total):
            if total == amount:
                return 0
            if total > amount:
                return float("inf")
            ans = float("inf")
            for coin in coins:
                ans = min(ans , dfs(total + coin) + 1)
            return ans
        ans = dfs(0)
        return ans if ans != float("inf") else -1
            
