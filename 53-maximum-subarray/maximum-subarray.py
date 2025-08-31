class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            curr = max(num , num + curr)
            max_sum = max(max_sum,curr)

        return max_sum