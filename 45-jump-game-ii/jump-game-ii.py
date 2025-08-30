class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            end_index_for_slice = min(i + nums[i], n - 1)
            s = dp[i + 1 : end_index_for_slice + 1]
            if s: 
                dp[i] = min(s) + 1
        return dp[0]