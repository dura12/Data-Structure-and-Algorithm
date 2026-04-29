# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            current = node

            # Find the leftmost leaf
            while current.left:
                current = current.left

            return current
        def help(node , key):
            if not node:
                return None
            if node.val > key:
                node.left = help(node.left , key)
            elif node.val < key:
                node.right = help(node.right , key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                minval = find_min(node.right)
                node.val = minval.val
                node.right = help(node.right , minval.val)
            return node
        return help(root, key)


            
            
