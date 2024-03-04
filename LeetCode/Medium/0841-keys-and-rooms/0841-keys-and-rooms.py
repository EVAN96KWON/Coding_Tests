class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False] * (len(rooms) - 1)
        q = rooms[0]

        while q:
            key = q.pop(0)
            visited[key] = True

            for n in rooms[key]:
                if not visited[n]:
                    q.append(n)

        return all(visited)
