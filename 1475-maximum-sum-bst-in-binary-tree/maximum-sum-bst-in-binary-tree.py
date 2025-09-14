# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return float('inf'), float('-inf'), 0, True

            l_min, l_max, l_sum, l_is_bst = dfs(node.left)
            r_min, r_max, r_sum, r_is_bst = dfs(node.right)

            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.ans = max(self.ans, total)
                return min(l_min, node.val), max(r_max, node.val), total, True
            else:
                return 0, 0, 0, False 

        dfs(root)
        return self.ans
