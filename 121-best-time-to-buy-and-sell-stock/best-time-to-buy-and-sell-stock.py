class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy , ans = float("inf") , float("-inf")
        for item in prices:
            buy = min(buy , item)
            ans = max(ans , item - buy)
        return ans
