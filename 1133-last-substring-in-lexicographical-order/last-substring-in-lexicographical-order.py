class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = ""
        t = s[-1:]
        for i in range(len(s) - 2, -1, -1):
            if s[i] < t[0]:
                ans = max(ans, t)
            t = s[i:]
        return max(ans, t)