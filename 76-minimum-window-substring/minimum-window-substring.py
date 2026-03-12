class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}

        for char in t:
            hash_t[char] = 1 + hash_t.get(char, 0)

        curr_count = 0
        need = len(hash_t)

        left = 0
        ans = float("inf")
        res = [-1, -1]

        for i in range(len(s)):
            c = s[i]
            hash_s[c] = 1 + hash_s.get(c, 0)

            if c in hash_t and hash_s[c] == hash_t[c]:
                curr_count += 1

            while curr_count == need:
                if (i - left + 1) < ans:
                    ans = i - left + 1
                    res = [left, i]

                hash_s[s[left]] -= 1
                if s[left] in hash_t and hash_s[s[left]] < hash_t[s[left]]:
                    curr_count -= 1

                left += 1

        l, r = res
        return s[l:r+1] if ans != float("inf") else ""