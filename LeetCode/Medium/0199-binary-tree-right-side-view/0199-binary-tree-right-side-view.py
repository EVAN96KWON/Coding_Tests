# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        hashmap = {} # k: level, v: node

        def dfs(node, level):
            if not node:
                return
            hashmap[level] = node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return list(hashmap.values())
