class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in ss:
                while s[right] != s[left]:
                    ss.remove(s[left])
                    left += 1
                ss.remove(s[right])
                left += 1
            ss.add(s[right])
            ans = max(ans , len(ss))
        return ans
        