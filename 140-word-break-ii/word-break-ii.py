class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        set_ = set(wordDict)
        self.ans = []
        def dfs(i , curr):
            if i == len(s):
                self.ans.append(" ".join(curr[::]))
                return 
            for j in range(i , len(s)):
                word = s[i : j + 1]
                if word in set_:
                    curr.append(word)
                    dfs(j + 1 , curr)
                    curr.pop()
            return 
        dfs(0 , [])
        print(self.ans)

        return self.ans
                