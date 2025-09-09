class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum =sum(nums[:k])
        result = window_sum
        left = 0
        for i in range(k , len(nums)):
            window_sum -= nums[i - k]
            window_sum += nums[i]
            result = max(result , window_sum)
        return result/k

            
