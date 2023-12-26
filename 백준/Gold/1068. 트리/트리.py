def count_leaves():
    return list(tree.values()).count([])


def delete_node(current_node):
    next_nodes = tree[current_node][:]

    if next_nodes:
        for next_node in next_nodes:
            delete_node(next_node)

    for k, v in tree.items():
        if current_node in v:
            v.remove(current_node)
    del tree[current_node]


if __name__ == '__main__':
    N = int(input())
    parents = list(map(int, input().split()))
    del_node = int(input())

    root = 0
    tree = {n: [] for n in range(N)}

    for i in range(len(parents)):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    delete_node(del_node)
    print(count_leaves())
