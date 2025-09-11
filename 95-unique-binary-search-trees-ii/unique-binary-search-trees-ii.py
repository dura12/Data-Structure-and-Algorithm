# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(l , r):
            if l == r:
                return [TreeNode(l)]
            if l > r:
                return [None]
            temp = []
            for root in range(l , r+1):
                left = dfs(l , root - 1)
                right = dfs(root + 1  , r)
                for s in left:
                    for g in right:
                        temp.append(TreeNode(root , s , g))
            return temp
        return dfs(1,n)
        return self.ans