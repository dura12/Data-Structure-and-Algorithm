from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counts2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counts2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num1 in self.nums1:
            target = tot - num1
            ans += self.counts2[target]
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)