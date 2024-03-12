class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        cnt = 0

        for i in range(len(visited)):
            if not visited[i]:
                cnt += 1
                queue = [i]

            while queue:
                city = queue.pop(0)
                visited[city] = True

                for j in range(len(isConnected)):
                    if isConnected[city][j] and not visited[j]:
                        visited[j] = True
                        queue.append(j)

        return cnt
