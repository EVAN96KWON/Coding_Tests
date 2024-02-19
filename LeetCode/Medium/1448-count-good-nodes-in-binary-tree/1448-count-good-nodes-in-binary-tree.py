# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, depth: int) -> int:
            if not node:
                return 0

            if node.val:
                if node.val >= depth:
                    return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
                else:
                    return dfs(node.left, depth) + dfs(node.right, depth)
            return dfs(node.left, depth) + dfs(node.right, depth)

        return dfs(root, root.val)