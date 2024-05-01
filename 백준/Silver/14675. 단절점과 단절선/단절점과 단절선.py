import sys
from collections import defaultdict

input = sys.stdin.readline


def is_cut_vertex(graph, v):
    return len(graph[v]) >= 2


def main():
    graph = defaultdict(list)

    N = int(input())
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t == 1:
            print("yes" if is_cut_vertex(graph, k) else "no")
        else:
            print("yes")


if __name__ == "__main__":
    main()
