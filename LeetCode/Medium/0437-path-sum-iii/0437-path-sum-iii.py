class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        self.count = 0
        self.cache = {}
        self.dfs(root, target, 0)
        return self.count

    def dfs(
        self,
        root: Optional[TreeNode],
        target: int,
        cur_path_sum: int,
    ):
        if root is None or root.val is None:
            return

        cur_path_sum += root.val

        if cur_path_sum == target:
            self.count += 1

        if cur_path_sum - target in self.cache:
            self.count += self.cache[cur_path_sum - target]

        self.cache[cur_path_sum] = self.cache.get(cur_path_sum, 0) + 1
        self.dfs(root.left, target, cur_path_sum)
        self.dfs(root.right, target, cur_path_sum)
        self.cache[cur_path_sum] = self.cache.get(cur_path_sum, 0) - 1
