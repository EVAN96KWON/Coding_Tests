# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        if not root:
            return

        if root in [p, q]:
            return node

        left, right = (
            self.lowestCommonAncestor(node.left),
            self.lowestCommonAncestor(node.right),
        )

        if left and right:
            return root

        return left or right

