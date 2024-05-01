import sys
from collections import defaultdict

input = sys.stdin.readline


def is_cut_vertex(tree, vertex: int) -> None:
    if len(tree[vertex]) < 2:
        print("no")
    else:
        print("yes")


def is_bridge(tree, edge) -> None:
    print("yes")


def main():
    tree = defaultdict(list)
    edges = [(0, 0)]

    N = int(input())
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        edges.append((a, b))

    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t == 1:
            is_cut_vertex(tree, k)
        else:
            is_bridge(tree, edges[k])


if __name__ == "__main__":
    main()
