class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        if len(nums) == 0:
            return []

        dIndices = []

        for j in range(len(nums)):

            if nums[j] == key:

                if j - k >= 0:
                    start = j - k

                else:
                    start = 0

                if len(dIndices) != 0 and start <= dIndices[-1]:
                    start = dIndices[-1] + 1

                if k + j < len(nums):
                    end = k + j

                else:
                    end = len(nums) - 1
            
                for i in range(start, end + 1):
                    dIndices.append(i)
        
        return dIndices
        