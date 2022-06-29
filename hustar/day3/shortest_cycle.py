from sys import maxsize

INF = int(0x3f3f3f3f)


class Edge:
    def __init__(self, u: int,
                 v: int,
                 weight: int) -> None:
        self.u = u
        self.v = v
        self.weight = weight


class Graph:
    def __init__(self, V: int) -> None:
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.edge = []

    def addEdge(self, u: int,
                v: int,
                w: int) -> None:

        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

        e = Edge(u, v, w)
        self.edge.append(e)

    def removeEdge(self, u: int,
                   v: int, w: int) -> None:

        self.adj[u].remove((v, w))
        self.adj[v].remove((u, w))

    # Find the shortest path from source
    # to sink using Dijkstra’s shortest
    # path algorithm [ Time complexity
    # O(E logV )]
    def ShortestPath(self, u: int, v: int) -> int:
        setds = set()
        dist = [INF] * self.V
        setds.add((0, u))
        dist[u] = 0

        while setds:
            tmp = setds.pop()

            uu = tmp[1]

            for i in self.adj[uu]:
                vv = i[0]
                weight = i[1]

                # If there is shorter path to v through u.
                if dist[vv] > dist[uu] + weight:
                    if dist[vv] != INF:
                        if (dist[vv], vv) in setds:
                            setds.remove((dist[vv], vv))

                    dist[vv] = dist[uu] + weight
                    setds.add((dist[vv], vv))

        # Return shortest path from
        # current source to sink
        return dist[v]

    def FindMinimumCycle(self) -> int:
        min_cycle = maxsize
        E = len(self.edge)

        for i in range(E):
            e = self.edge[i]
            self.removeEdge(e.u, e.v, e.weight)
            distance = self.ShortestPath(e.u, e.v)
            min_cycle = min(min_cycle, distance + e.weight)
            self.addEdge(e.u, e.v, e.weight)

        return min_cycle if min_cycle < INF else -1


def main():
    for TC in range(int(input())):
        V, E = map(int, input().split())

        g = Graph(V)

        for m in range(E):
            u, v = map(int, input().split())
            g.addEdge(u, v, 1)

        print(g.FindMinimumCycle())


if __name__ == '__main__':
    main()

'''
3
3 3
0 1
1 2
0 2
5 6
0 1
1 2
1 3
3 2
2 4
4 1
3 2
0 1
1 2
'''
