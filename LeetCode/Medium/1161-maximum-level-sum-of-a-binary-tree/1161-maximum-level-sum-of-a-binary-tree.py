# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)

        def bfs(root, level):
            if root is None or root.val is None:
                return

            level_sum[level] += root.val

            bfs(root.left, level + 1)
            bfs(root.right, level + 1)

        bfs(root, 1)

        return max(level_sum, key=level_sum.get)
