class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, e in connections:
            graph[s].append((e, True))
            graph[e].append((s, False))

        queue = [(0, False)]
        res = 0
        visited = set()
        while queue:
            node, can_reach = queue.pop(0)
            if can_reach:
                res += 1
            visited.add(node)
            for e, can_reach in graph[node]:
                if e not in visited:
                    queue.append((e, can_reach))

        return res
