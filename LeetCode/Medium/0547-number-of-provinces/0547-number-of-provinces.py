class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)

        def dfs(i: int) -> None:
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)

        cnt = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                cnt += 1

        return cnt
