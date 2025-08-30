class Solution:
    def longestValidParentheses(self, s: str) -> int:
        r = 0
        stack = [-1]
        count = 0
        ans = 0
        while r < len(s):
            if s[r] == "(":
                stack.append(r)
            if s[r] == ")":
                stack.pop()
                if not stack:
                    stack.append(r)
                else:
                    ans = max(ans , r - stack[-1])
            r += 1
        return ans
            