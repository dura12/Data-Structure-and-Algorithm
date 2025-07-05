class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = -1 
        for key , val in c.items():
            if key == val:
                ans = max(ans , key)

        return ans

