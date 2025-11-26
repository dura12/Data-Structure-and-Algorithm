# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node , path , sum_):
            if not node:
                return 
            if not node.left and not node.right:
                
                if sum_ == node.val:
                    ans.append(path.copy() + [node.val])
                    return 
            # if sum_ < 0:
            #     return 
            path.append(node.val)
            sum_ -= node.val
            dfs(node.left , path , sum_)
            dfs(node.right , path , sum_)
            path.pop()
            sum_ += node.val
            return 
        dfs(root , [] , targetSum)
        return ans
