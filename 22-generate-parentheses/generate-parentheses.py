class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr_string, open_count, close_count):
            if len(curr_string) == 2 * n:
                ans.append(curr_string)
                return
            if open_count < n:
                backtrack(curr_string + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr_string + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return ans