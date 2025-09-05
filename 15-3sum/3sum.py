class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_two_num = nums[left] + nums[right] 
                if sum_two_num == -nums[i]:
                    ans.append([nums[left],nums[right],nums[i]])
                    left += 1
                    right -= 1
                    while (left < right) and nums[left - 1] == nums[left]:
                        left += 1
                elif sum_two_num + nums[i] > 0:
                    right -= 1

                else:
                    left += 1
        return ans
                
    
       
