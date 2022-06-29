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

        e = Edge(u, v, w)
        self.edge.append(e)

    # using Dijkstra’s shortest path algorithm
    # Time complexity O(E logV)
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

                if dist[vv] > dist[uu] + weight:
                    if dist[vv] != INF:
                        if (dist[vv], vv) in setds:
                            setds.remove((dist[vv], vv))

                    dist[vv] = dist[uu] + weight
                    setds.add((dist[vv], vv))

        return dist[v] if dist[v] < INF else -1


def main():
    for TC in range(int(input())):
        V, E = map(int, input().split())
        g = Graph(V)

        for e in range(E):
            u, v, w = map(int, input().split())
            g.addEdge(u, v, w)

        print(g.ShortestPath(0, V - 1))


if __name__ == '__main__':
    main()

'''
3
4 4
0 1 3
0 2 4
2 1 2
1 3 1
4 4
0 1 1
2 0 3
1 2 5
3 1 4
6 12
0 1 7
1 2 3
2 0 1
0 3 4
2 3 5
3 2 1
3 4 8
4 3 1
2 4 2
1 4 4
4 5 2
3 5 9
'''