import sys
from collections import defaultdict

input = sys.stdin.readline


def preorder(node, visited=list()):
    if node in visited:
        return

    left, right = graph[node]

    visited.append(node)
    preorder(left, visited) if left.isalpha() else ...
    preorder(right, visited) if right.isalpha() else ...

    return visited


def inorder(node, visited=list()):
    if node in visited:
        return

    left, right = graph[node]

    inorder(left, visited) if left.isalpha() else ...
    visited.append(node)
    inorder(right, visited) if right.isalpha() else ...

    return visited


def postorder(node, visited=list()):
    if node in visited:
        return

    left, right = graph[node]

    postorder(left, visited) if left.isalpha() else ...
    postorder(right, visited) if right.isalpha() else ...
    visited.append(node)

    return visited


if __name__ == "__main__":
    N = int(input())
    graph = defaultdict(tuple)
    for _ in range(N):
        n, l, r = input().split()
        graph[n] = (l, r)

    print("".join(preorder("A")))
    print("".join(inorder("A")))
    print("".join(postorder("A")))
