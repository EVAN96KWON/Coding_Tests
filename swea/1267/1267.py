def dfs(graph, start_node, required):
    visit = list()
    queue = list()

    queue.extend(start_node)

    while queue:
        # no require or requirement satisfied at this node
        if required[queue[0]] == [] or set(required[queue[0]]) <= set(visit):
            node = queue.pop(0)
            if node not in visit:
                visit.append(node)
                queue.extend(graph[node])
        # shuffle queue
        else:
            queue.append(queue.pop(0))

    return list(map(str, visit))


T = 10

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [_ for _ in input().split()]
    graph = {_: [] for _ in range(1, V + 1)}
    required = {_: [] for _ in range(1, V + 1)}

    # init graph & required dict
    while lst:
        start = int(lst.pop(0))
        to = int(lst.pop(0))
        graph[start].append(to)
        required[to].append(start)

    # find start_node which requires nothing
    start_nodes = list()
    for i in range(1, len(required) + 1):
        if not required[i]:
            start_nodes.append(i)

    print(f'#{test_case} ' + ' '.join(dfs(graph, start_nodes, required)))
