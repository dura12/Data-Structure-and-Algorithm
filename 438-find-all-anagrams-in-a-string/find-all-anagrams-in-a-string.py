class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        dic1 = Counter(p)
        window = Counter(s[:k])
        
        ans = []
        if window == dic1:
            ans.append(0)
        for i in range(k,len(s)):
            window[s[i-k]] -= 1
            window[s[i]] += 1
            if (window == dic1):
                ans.append(i-k + 1)
        return ans


 